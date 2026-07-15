from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ==========================================================
    # Application
    # ==========================================================

    APP_NAME: str = "KnowledgeForge"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"

    # ==========================================================
    # Logging
    # ==========================================================

    LOG_LEVEL: str = "INFO"

    # ==========================================================
    # Ollama
    # ==========================================================

    OLLAMA_BASE_URL: str = Field(
        description="Base URL of the Ollama server.",
    )

    # ==========================================================
    # OpenAI
    # ==========================================================

    OPENAI_API_KEY: str | None = None

    # ==========================================================
    # Default AI Configuration
    # ==========================================================

    DEFAULT_PROVIDER: str = Field(
        description="Default LLM provider.",
    )

    DEFAULT_MODEL: str = Field(
        description="Default LLM model.",
    )

    DEFAULT_TEMPERATURE: float = Field(
        ge=0.0,
        le=2.0,
        description="Default sampling temperature.",
    )

    DEFAULT_MAX_TOKENS: int = Field(
        gt=0,
        description="Default maximum output tokens.",
    )

    DEFAULT_TOP_P: float = Field(
        ge=0.0,
        le=1.0,
        description="Default nucleus sampling value.",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """
    return Settings()


settings = get_settings()