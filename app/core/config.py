from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.
    """

    APP_NAME: str = "KnowledgeForge"
    APP_VERSION: str = "0.1.0"

    DEFAULT_PROVIDER: str = "openai"
    DEFAULT_MODEL: str = "gpt-5-mini"

    TEMPERATURE: float = Field(
        default=0.2,
        ge=0.0,
        le=2.0,
    )

    MAX_TOKENS: int = Field(
        default=4000,
        gt=0,
    )

    OPENAI_API_KEY: str | None = None
    GOOGLE_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    OPENROUTER_API_KEY: str | None = None

    OLLAMA_BASE_URL: str = "http://localhost:11434"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()