from __future__ import annotations

from fastapi import APIRouter

from app.agents.knowledge import KnowledgeAgent
from app.agents.reflection import ReflectionAgent
from app.ai.service import LLMService
from app.api.schemas.youtube import (
    YouTubeRequest,
    YouTubeResponse,
)
from app.core.config import settings
from app.ingestion.youtube import YouTubeTranscriptService
from app.workflow.youtube_learning import YouTubeLearningWorkflow
from app.exporters.markdown import MarkdownExporter

router = APIRouter(
    prefix="/api/v1/youtube",
    tags=["YouTube"],
)


llm_service = LLMService()

transcript_service = YouTubeTranscriptService()

knowledge_agent = KnowledgeAgent(
    llm_service=llm_service,
    settings=settings,
)

reflection_agent = ReflectionAgent(
    llm_service=llm_service,
    settings=settings,
)

markdown_exporter = MarkdownExporter(
    output_directory=settings.OUTPUT_DIRECTORY,
)

workflow = YouTubeLearningWorkflow(
    transcript_service=transcript_service,
    knowledge_agent=knowledge_agent,
    reflection_agent=reflection_agent,
    markdown_exporter=markdown_exporter,
)


@router.post(
    "",
    response_model=YouTubeResponse,
    summary="Process a YouTube video",
)
async def process_youtube(
    request: YouTubeRequest,
) -> YouTubeResponse:
    """
    Transform a YouTube video into structured knowledge
    and a learning reflection.
    """

    result = await workflow.run(request.url)

    return YouTubeResponse(
    source_url=result.transcript.source_url,
    video_id=result.transcript.video_id,
    title=result.knowledge.title,
    knowledge=result.knowledge.markdown,
    reflection=result.reflection.markdown,
    )