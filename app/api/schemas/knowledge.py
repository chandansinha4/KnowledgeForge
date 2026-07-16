from __future__ import annotations

from pydantic import BaseModel, Field


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
    Response returned after generating structured knowledge.
    """

    title: str = Field(
        description="Title extracted from the generated Markdown.",
    )

    markdown: str = Field(
        description="Generated knowledge in Markdown format.",
    )