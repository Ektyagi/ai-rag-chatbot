from uuid import uuid4

from fastapi import UploadFile

from app.services.chunk_service import split_text
from app.services.file_service import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf
from app.services.vector_store import vector_store


def process_document(file: UploadFile):

    saved_path = save_uploaded_file(file)

    extracted_text = extract_text_from_pdf(saved_path)

    chunks = split_text(extracted_text)

    ids = [str(uuid4()) for _ in chunks]

    metadatas = [
        {
            "source": file.filename,
            "chunk": i,
            "file_path": saved_path
        }
        for i in range(len(chunks))
    ]

    vector_store.add_texts(
        texts=chunks,
        metadatas=metadatas,
        ids=ids
    )

    return {
        "filename": file.filename,
        "saved_path": saved_path,
        "total_chunks": len(chunks)
    }