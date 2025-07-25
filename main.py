from fastapi import FastAPI, File, UploadFile
from app.ocr_engine import process_image
from app.pdf_parser import save_pdf

app = FastAPI()

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    content = await file.read()
    text = process_image(content)
    return {"text": text}

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    result = save_pdf(file)
    return {"status": result}
