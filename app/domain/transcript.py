from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TranscriptDocument:
    """
    Transcript extracted from a learning resource.
    """

    title: str

    transcript: str

    video_id: str

    source_url: str