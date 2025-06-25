# 🧠 EasyOCR Text Recognition API

A lightweight, free, and powerful OCR (Optical Character Recognition) API built using **EasyOCR** and **FastAPI**. This API can accurately recognize both **printed** and **handwritten** English text from a variety of image formats.

---

## 🚀 Features

- 🔤 **Text Extraction**: Supports common image formats including `.jpg`, `.jpeg`, `.png`, and more.
- 📋 **Structured Output**: Returns plain text as well as detailed data — including bounding boxes, recognized text, and confidence scores.
- 🧠 **EasyOCR Engine**: Utilizes the EasyOCR library for high-quality text recognition, without requiring a GPU.
- ⚡ **FastAPI Backend**: Fast, asynchronous, and production-ready Python API framework.
- 🔗 **RESTful API Interface**: Includes interactive Swagger UI documentation at `/docs`.
- 🌍 **Deploy Anywhere**: Easily deployable on platforms like [Railway](https://railway.app/), [Render](https://render.com), or even on your own server.

---

## 🛠️ Tech Stack

- 🐍 Python 3.8+
- ⚡ FastAPI for API development
- 🔍 EasyOCR for optical character recognition
- 🧵 Uvicorn as the ASGI server

---

## 📦 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/easyocr-api.git
cd easyocr-api
pip install -r requirements.txt
```

---

## ⚙️ How to run
 - Run the server locally:
   - uvicorn main:app --reload

 - Test the API in your browser:
   - http://localhost:8000/docs

---

