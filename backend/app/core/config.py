from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    CHROMA_COLLECTION_NAME: str = "company_documents"

    class Config:
        env_file = ".env"


settings = Settings()