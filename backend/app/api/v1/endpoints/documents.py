from fastapi import APIRouter, UploadFile, File

from app.services.file_service import save_uploaded_file

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    saved_path = save_uploaded_file(file)

    return {
        "filename": file.filename,
        "saved_path": saved_path,
        "content_type": file.content_type
    }