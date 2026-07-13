from enum import Enum

from pydantic import BaseModel, Field


class Provider(str, Enum):
    """
    Supported LLM providers.
    """

    OPENAI = "openai"
    GEMINI = "gemini"
    ANTHROPIC = "anthropic"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    """
    Represents a single chat message.
    """

    role: Role

    content: str

    @classmethod
    def system(cls, content: str) -> "Message":
        return cls(
            role=Role.SYSTEM,
            content=content,
        )

    @classmethod
    def user(cls, content: str) -> "Message":
        return cls(
            role=Role.USER,
            content=content,
        )

    @classmethod
    def assistant(cls, content: str) -> "Message":
        return cls(
            role=Role.ASSISTANT,
            content=content,
        )


class GenerationConfig(BaseModel):
    """
    Controls how the LLM generates responses.
    """

    temperature: float = Field(
        default=0.2,
        ge=0.0,
        le=2.0,
    )

    max_tokens: int = Field(
        default=4000,
        gt=0,
    )

    top_p: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
    )

    stream: bool = False

    response_format: str | None = None


class ChatRequest(BaseModel):
    """
    Standard request sent to the LLM service.
    """

    provider: Provider

    model: str

    messages: list[Message] = Field(
        min_length=1
    )

    generation_config: GenerationConfig = Field(
        default_factory=GenerationConfig
    )

class TokenUsage(BaseModel):
    """
    Token usage statistics.
    """

    input_tokens: int | None = None

    output_tokens: int | None = None

    total_tokens: int | None = None


class ChatResponse(BaseModel):
    """
    Standard response returned by the LLM service.
    """

    content: str

    provider: Provider

    model: str

    usage: TokenUsage | None = None

    response_metadata: dict = Field(
        default_factory=dict
    )


class HealthStatus(BaseModel):
    """
    Health status of an LLM provider.
    """

    healthy: bool

    provider: Provider

    model: str

    latency_ms: float | None = None

    message: str | None = None