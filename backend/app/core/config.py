from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    OPENAI_API_KEY: str = ""
    GEMINI_API_KEY: str = ""

    DATABASE_URL: str = ""

    CHROMA_DB_PATH: str = "vectorstore"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()