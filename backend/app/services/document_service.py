from fastapi import UploadFile

from app.services.file_service import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import split_text


def process_document(file: UploadFile):
    """
    Complete document processing pipeline.
    """

    saved_path = save_uploaded_file(file)

    extracted_text = extract_text_from_pdf(saved_path)

    chunks = split_text(extracted_text)

    return {
        "filename": file.filename,
        "saved_path": saved_path,
        "chunks": chunks
    }