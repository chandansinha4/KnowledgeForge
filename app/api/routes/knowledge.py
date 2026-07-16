from __future__ import annotations

from fastapi import APIRouter

from app.agents.knowledge import KnowledgeAgent
from app.ai.service import LLMService
from app.api.schemas.knowledge import (
    KnowledgeRequest,
    KnowledgeResponse,
)
from app.core.config import settings

router = APIRouter(
    prefix="/api/v1/knowledge",
    tags=["Knowledge"],
)

llm_service = LLMService()
knowledge_agent = KnowledgeAgent(
    llm_service=llm_service,
    settings=settings,
)


@router.post(
    "",
    response_model=KnowledgeResponse,
    summary="Generate structured knowledge notes",
)
async def generate_knowledge(
    request: KnowledgeRequest,
) -> KnowledgeResponse:
    """
    Convert raw text into structured Markdown study notes.
    """


    document = await knowledge_agent.generate(request.text)

    return KnowledgeResponse(
        title=document.title,
        markdown=document.markdown,
    )