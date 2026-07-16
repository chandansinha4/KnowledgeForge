from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ReflectionDocument:
    """
    Structured learning reflection generated from a KnowledgeDocument.
    """

    title: str

    markdown: str