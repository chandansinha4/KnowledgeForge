from __future__ import annotations

from pydantic import BaseModel, Field

from app.ai.models import Provider


class KnowledgeRequest(BaseModel):
    """
    Request body for knowledge generation.
    """

    text: str = Field(
        ...,
        min_length=1,
        max_length=10_000,
        description="Raw text to transform into structured knowledge notes.",
    )



class KnowledgeResponse(BaseModel):
    """
    Response returned by the Knowledge Agent.
    """

    content: str

    provider: Provider

    model: str

    input_tokens: int | None = None

    output_tokens: int | None = None

    total_tokens: int | None = None