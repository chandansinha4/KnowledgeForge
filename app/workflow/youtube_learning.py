from __future__ import annotations

from app.agents.knowledge import KnowledgeAgent
from app.agents.reflection import ReflectionAgent
from app.domain.learning import LearningDocument
from app.exporters.markdown import MarkdownExporter
from app.ingestion.youtube import YouTubeTranscriptService


class YouTubeLearningWorkflow:
    """
Coordinates the complete YouTube learning pipeline.
    """

    def __init__(
        self,
        transcript_service: YouTubeTranscriptService,
        knowledge_agent: KnowledgeAgent,
        reflection_agent: ReflectionAgent,
        markdown_exporter: MarkdownExporter,
    ) -> None:
        self._transcript_service = transcript_service
        self._knowledge_agent = knowledge_agent
        self._reflection_agent = reflection_agent
        self._markdown_exporter = markdown_exporter

    async def run(
        self,
        url: str,
    ) -> LearningDocument:
        """
        Transform a YouTube video into a complete learning document
        and export the generated Markdown files.
        """

        transcript = self._transcript_service.ingest(url)

        knowledge = await self._knowledge_agent.generate(
            transcript.transcript
        )

        reflection = await self._reflection_agent.generate(
            knowledge
        )

        self._markdown_exporter.export_knowledge(
            knowledge,
            transcript,
        )

        self._markdown_exporter.export_reflection(
            reflection,
            transcript,
        )

        return LearningDocument(
            transcript=transcript,
            knowledge=knowledge,
            reflection=reflection,
        )