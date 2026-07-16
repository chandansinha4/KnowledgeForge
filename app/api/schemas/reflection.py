from pydantic import BaseModel, Field


class ReflectionRequest(BaseModel):
    """
    Request for generating learning reflections.
    """

    text: str = Field(
        ...,
        min_length=1,
        description="Educational text to generate reflections from.",
    )

class ReflectionResponse(BaseModel):
    """
    Reflection generated from educational content.
    """

    title: str = Field(
        description="Reflection title.",
    )

    markdown: str = Field(
        description="Generated reflection in Markdown format.",
    )