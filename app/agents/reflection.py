from __future__ import annotations

from app.ai.models import (
    ChatRequest,
    Message,
    Provider,
)
from app.ai.prompts.reflection import REFLECTION_PROMPT
from app.ai.service import LLMService
from app.core.config import Settings
from app.domain.knowledge import KnowledgeDocument
from app.domain.reflection import ReflectionDocument


class ReflectionAgent:
    """
    Agent responsible for generating learning reflections from structured knowledge.
    """

    def __init__(
        self,
        llm_service: LLMService,
        settings: Settings,
    ) -> None:
        self._llm_service = llm_service
        self._settings = settings


    async def generate(
    self,
    knowledge: KnowledgeDocument,
    ) -> ReflectionDocument:
        """
        Generate learning reflections from a KnowledgeDocument.
        """


        prompt = REFLECTION_PROMPT.invoke(
            {
                "knowledge": knowledge.markdown,
            }
        )

        messages = []

        for message in prompt.messages:

            if message.type == "system":
                messages.append(
                    Message.system(message.content)
                )

            elif message.type == "human":
                messages.append(
                    Message.user(message.content)
                )

        request = ChatRequest(
            provider=Provider(
            self._settings.DEFAULT_PROVIDER
            ),
            model=self._settings.DEFAULT_MODEL,
            messages=messages,
        )

        response = await self._llm_service.generate(request)

        return ReflectionDocument(
            title=knowledge.title,
            markdown=response.content,
        )