from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=settings.CHUNK_SIZE,
    chunk_overlap=settings.CHUNK_OVERLAP,
)