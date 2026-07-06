from fastapi import APIRouter, UploadFile, File

from app.services.document_service import process_document

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    result = process_document(file)

    return {
        "filename": result["filename"],
        "saved_path": result["saved_path"],
        "total_chunks": len(result["chunks"]),
        "preview": result["chunks"][:3]
    }