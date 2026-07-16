from __future__ import annotations

from fastapi import APIRouter

from app.agents.knowledge import KnowledgeAgent
from app.agents.reflection import ReflectionAgent
from app.ai.service import LLMService
from app.api.schemas.reflection import (
    ReflectionRequest,
    ReflectionResponse,
)
from app.core.config import settings

router = APIRouter(
    prefix="/api/v1/reflection",
    tags=["Reflection"],
)

llm_service = LLMService()

knowledge_agent = KnowledgeAgent(
    llm_service=llm_service,
    settings=settings,
)

reflection_agent = ReflectionAgent(
    llm_service=llm_service,
    settings=settings,
)


@router.post(
    "",
    response_model=ReflectionResponse,
    summary="Generate learning reflections",
)
async def generate_reflection(
    request: ReflectionRequest,
) -> ReflectionResponse:
    """
    Generate learning reflections from educational text.
    """

    knowledge_document = await knowledge_agent.generate(
        request.text,
    )

    reflection_document = await reflection_agent.generate(
        knowledge_document,
    )

    return ReflectionResponse(
        title=reflection_document.title,
        markdown=reflection_document.markdown,
    )