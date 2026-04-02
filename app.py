# fastapi
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch 
import re
from pathlib import Path
from fastapi.templating import Jinja2Templates #UI
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles

#initialize our fastapi app
app=FastAPI(title="Text summarizer APP",description="Text summarization using T5",version="1.0")

# base dir (project root)
BASE_DIR = Path(__file__).resolve().parent

# model & Tokenizer
MODEL_DIR = BASE_DIR / "model"
model = T5ForConditionalGeneration.from_pretrained(str(MODEL_DIR))
tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR), use_fast=True)

#device 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(device)

# templating 
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

#Input Schema for Dialouge => string
class DialogueInput(BaseModel):
    dialogue: str

#clean_data
def clean_data(text):
  text=re.sub(r"\r\n"," ",text) #lines
  text=re.sub(r"\s+"," ",text) # spaces
  text=re.sub(r"<.*?>"," ",text) # html tags <p> <h>
  text=text.strip().lower()
  return text

#summarization function

def summarize_dialogue(dialogue:str)->str:
  dialogue = clean_data(dialogue) #clean
  #tokenize
  inputs = tokenizer(
      dialogue,
      padding="max_length",
      max_length=512,
      truncation=True,
      return_tensors="pt"
  ).to(device)

  #generate the summary => token ids
  with torch.no_grad():
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=6,
        length_penalty=1.5,
        no_repeat_ngram_size=3,
        early_stopping=True
    )

  #token ids convert to summary => decoding
  summary=tokenizer.decode(targets[0],skip_special_tokens=True) #EOS,SEP
  return summary

#API endpoint for summarization
@app.post("/summarize")
async def summarize(dialogue_input: DialogueInput):
   summary = summarize_dialogue(dialogue_input.dialogue)
   return {"summary": summary}

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
   return templates.TemplateResponse(request, "index.html", {"request": request})
