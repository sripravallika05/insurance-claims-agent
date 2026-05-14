from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.pdf_extractor import extract_text_from_pdf
from app.services.field_extractor import extract_fields
from app.services.validator import validate_fields
from app.services.router import determine_route
from app.services.reasoning import generate_reasoning

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.get("/")
def home():
    return {"message": "Insurance Claims API Running"}


@router.post("/process-claim")
async def process_claim(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    extracted_fields = extract_fields(text)

    missing_fields = validate_fields(extracted_fields)

    route = determine_route(extracted_fields, missing_fields)

    reasoning = generate_reasoning(route)

    return {
        "extractedFields": extracted_fields,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reasoning
    }