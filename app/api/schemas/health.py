from __future__ import annotations

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """
    Health response returned by the API.
    """

    status: str = Field(
        description="Current application health status.",
    )

    app: str = Field(
        description="Application name.",
    )

    version: str = Field(
        description="Application version.",
    )

    environment: str = Field(
        description="Current application environment.",
    )

    provider: str = Field(
        description="Default AI provider.",
    )

    model: str = Field(
        description="Default AI model.",
    )