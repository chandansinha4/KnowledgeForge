from __future__ import annotations

from dataclasses import dataclass

from app.domain.knowledge import KnowledgeDocument
from app.domain.reflection import ReflectionDocument
from app.domain.transcript import TranscriptDocument


@dataclass(slots=True)
class LearningDocument:
    """
    Complete learning output generated from a YouTube video.
    """

    transcript: TranscriptDocument
    knowledge: KnowledgeDocument
    reflection: ReflectionDocument