from fastapi import APIRouter, UploadFile, File

from app.services.file_service import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    saved_path = save_uploaded_file(file)

    extracted_text = extract_text_from_pdf(saved_path)

    return {
        "filename": file.filename,
        "saved_path": saved_path,
        "content_type": file.content_type,
        "text": extracted_text
    }