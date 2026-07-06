from pathlib import Path
import shutil
from uuid import uuid4
from fastapi import UploadFile


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def save_uploaded_file(file: UploadFile) -> str:
    """
    Save the uploaded file with a unique filename.
    Returns the saved file path.
    """

    file_extension = Path(file.filename).suffix
    unique_filename = f"{uuid4()}{file_extension}"

    file_path = UPLOAD_DIR / unique_filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path)