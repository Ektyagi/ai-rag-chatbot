from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from app.core.config import settings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=settings.GEMINI_API_KEY,
)

vector_store = Chroma(
    persist_directory=settings.CHROMA_DB_PATH,
    embedding_function=embeddings,
)