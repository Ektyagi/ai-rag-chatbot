from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=settings.CHUNK_SIZE,
    chunk_overlap=settings.CHUNK_OVERLAP,
)


def split_text(text: str) -> list[str]:
    """
    Split extracted text into overlapping chunks.
    """
    return text_splitter.split_text(text)