# 🧠 EasyOCR Text Recognition API

A free and efficient OCR (Optical Character Recognition) API built using **EasyOCR** and **FastAPI**, capable of recognizing both **printed** and **handwritten** English text from images.

---

## 🚀 Features

- 🔤 Extracts text from images (JPG, PNG, etc.)
- 📋 Returns both **raw text** and **detailed structured results** (with bounding boxes & confidence scores)
- 🧠 Powered by **EasyOCR** (no GPU required)
- 🔗 RESTful API with Swagger documentation
- 🌍 Deployable for **free** using [Railway](https://railway.app/)

---

## 🛠️ Tech Stack

- 🐍 Python 3.8+
- ⚡ FastAPI
- 🔍 EasyOCR
- 📦 Uvicorn ASGI server

---

## 📦 Installation

1. **Clone and install requirements:**

```bash
git clone https://github.com/yourusername/easyocr-api.git
cd easyocr-api
pip install -r requirements.txt

```

## ⚙️ How to run
 - Run the server locally:
   - uvicorn main:app --reload

 - Test the API in your browser:
   - http://localhost:8000/docs

---

