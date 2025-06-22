from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import easyocr
import io
import numpy as np

# Initialize FastAPI app with metadata
app = FastAPI(
    title="EasyOCR Image Text Recognition API",
    description="A free OCR API using EasyOCR that works for both printed and handwritten text.",
    version="1.0.0"
)

# Initialize EasyOCR reader (no GPU needed)
reader = easyocr.Reader(['en'], gpu=False)

# Allow cross-origin requests (for frontend or mobile app access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
async def root():
    """
    Root endpoint to verify the API is live.
    """
    return {"message": "EasyOCR API is up and running."}


@app.post("/ocr", tags=["OCR"])
async def ocr_image(file: UploadFile = File(...)):
    """
    Perform OCR and return structured text with bounding boxes and confidence.

    Request:
    - file: an image file (.jpg, .png, etc.)

    Response:
    - JSON with each text, bounding box, and confidence score
    """
    try:
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        image_np = np.array(image)
        results = reader.readtext(image_np)

        # 👇 Use this logic to convert output
        extracted = []
        for res in results:
            bbox = [[float(coord) for coord in point] for point in res[0]]
            text = res[1]
            confidence = float(res[2])
            extracted.append({
                "text": text,
                "confidence": confidence,
                "bounding_box": bbox
            })

        return JSONResponse(content={"results": extracted})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/ocr/raw-text", tags=["OCR"])
async def ocr_raw_text(file: UploadFile = File(...)):
    """
    Perform OCR and return only the full text (no bounding boxes).

    Request:
    - file: an image file (.jpg, .png, etc.)

    Response:
    - JSON with the full concatenated text
    """
    try:
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")

        # ✅ Convert to NumPy array for EasyOCR
        image_np = np.array(image)

        # ✅ Perform OCR
        results = reader.readtext(image_np)

        # ✅ Extract only the text parts
        full_text = ' '.join([res[1] for res in results])

        return JSONResponse(content={"text": full_text})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

