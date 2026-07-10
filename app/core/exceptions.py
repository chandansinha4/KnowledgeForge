"""
Custom exceptions used throughout the KnowledgeForge application.
"""


class KnowledgeForgeError(Exception):
    """
    Base exception for the application.
    """


class LLMError(KnowledgeForgeError):
    """
    Raised when an LLM request fails.
    """


class TranscriptError(KnowledgeForgeError):
    """
    Raised when a transcript cannot be retrieved.
    """


class PublishingError(KnowledgeForgeError):
    """
    Raised when publishing to an external service fails.
    """


class VectorStoreError(KnowledgeForgeError):
    """
    Raised when interacting with the vector database fails.
    """