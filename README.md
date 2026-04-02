# 🧠 T5 Text Summarizer 

An end-to-end text summarization system built using a fine-tuned T5 transformer model, deployed with FastAPI and a simple HTML interface.

---

## 📌 Overview

This project demonstrates how to build, fine-tune, and deploy a transformer-based NLP model for abstractive text summarization. It integrates model training, backend API development, and a lightweight frontend.

---

## 🚀 Features

* Fine-tuned T5 model for text summarization
* FastAPI backend for serving predictions
* HTML frontend for user interaction
* Clean and modular project structure

---

## 🛠 Tech Stack

* Python
* FastAPI
* Hugging Face Transformers
* PyTorch
* Jinja2
* HTML/CSS

---

## 📁 Project Structure

```id="p2zcck"
TEXTSUMMARIZERAPP/
│
├── app.py                  # FastAPI application
├── templates/              # HTML templates
│   └── index.html
│
├── model/                  # Model artifacts
│   ├── config.json
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
├── notebook/               # Training notebook
│   └── TextSummarizer.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```id="1f0ts8"
git clone https://github.com/LikithaKodidela/t5-text-summarizer-fastapi.git
cd t5-text-summarizer-fastapi
```

### 2. Create environment (optional)

```id="3vlj9c"
conda create -n summarizer python=3.11
conda activate summarizer
```

### 3. Install dependencies

```id="0e9nlm"
pip install -r requirements.txt
```

### 4. Run the application

```id="hmw2ej"
uvicorn app:app --reload
```

### 5. Open in browser

```id="7spuoa"
http://127.0.0.1:8000
```

---

## 🧪 Example

**Input:**

```id="v4m0nf"
Artificial Intelligence is transforming industries by enabling automation and data-driven decision making.
```

**Output:**

```id="i9p1mz"
AI is transforming industries by improving automation and decision-making.
```

---

## ⚠️ Notes

* The model weights (`.safetensors`) are not included due to GitHub size limits
* Load the model locally or from a model hosting platform (e.g., Hugging Face)

---

## 🔮 Future Improvements

* Deploy the application to cloud platforms
* Enhance UI/UX
* Add REST API endpoint for integration
* Support longer and multi-language inputs

---

## 👩‍💻 Author

Likitha Kodidela
