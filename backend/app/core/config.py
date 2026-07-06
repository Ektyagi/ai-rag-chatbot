from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI RAG Chatbot"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    GEMINI_API_KEY: str

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    CHROMA_COLLECTION_NAME: str = "company_documents"
    CHROMA_DB_PATH: str = "vectorstore"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()