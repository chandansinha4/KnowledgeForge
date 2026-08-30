from pydantic import BaseModel, Field


class YouTubeRequest(BaseModel):
    """
    Request for processing a YouTube video.
    """

    url: str = Field(
        ...,
        min_length=1,
        description="YouTube video URL.",
    )


class YouTubeResponse(BaseModel):
    """
    Complete learning output generated from a YouTube video.
    """

    source_url: str = Field(
        description="Original YouTube video URL.",
    )

    video_id: str = Field(
        description="YouTube video ID.",
    )

    title: str = Field(
        description="Title of the generated knowledge document.",
    )

    knowledge: str = Field(
        description="Structured knowledge in Markdown.",
    )

    reflection: str = Field(
        description="Learning reflection in Markdown.",
    )