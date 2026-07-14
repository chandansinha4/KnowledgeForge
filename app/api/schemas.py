from __future__ import annotations

from pydantic import BaseModel, Field

from app.ai.models import Provider


class ChatAPIRequest(BaseModel):
    """
    Request body for the chat endpoint.
    """

    prompt: str = Field(
        ...,
        min_length=1,
        description="User prompt.",
    )

    provider: Provider = Field(
        default=Provider.OLLAMA,
        description="LLM provider.",
    )

    model: str = Field(
        default="gemma3:1b",
        description="Model name.",
    )


class ChatAPIResponse(BaseModel):
    """
    Response returned by the chat endpoint.
    """

    content: str

    provider: Provider

    model: str

    input_tokens: int | None = None

    output_tokens: int | None = None

    total_tokens: int | None = None