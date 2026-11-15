
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application Settings
    app_name: str = "YojanaAI"
    app_version: str = "0.1.0"
    environment: str = "development"

    # API Settings
    gemini_api_key: str | None = None

    # Text Chunking Settings
    chunk_size: int = 800
    chunk_overlap: int = 150

    # Embedding Settings
    embedding_model: str = "intfloat/multilingual-e5-small"
    embedding_dim: int = 384

    # Qdrant Settings
    qdrant_url: str | None = "http://localhost:6333"
    qdrant_path: str | None = None
    qdrant_collection: str = "schemes"

    # Environment Configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
