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

    response = await knowledge_agent.generate(
        text=request.text,
    )

    return KnowledgeResponse(
        content=response.content,
        provider=response.provider,
        model=response.model,
        input_tokens=(
            response.usage.input_tokens
            if response.usage
            else None
        ),
        output_tokens=(
            response.usage.output_tokens
            if response.usage
            else None
        ),
        total_tokens=(
            response.usage.total_tokens
            if response.usage
            else None
        ),
    )