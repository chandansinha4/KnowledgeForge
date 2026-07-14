from __future__ import annotations

from app.ai.models import (
    ChatRequest,
    ChatResponse,
    Message,
    Provider,
)
from app.ai.prompts.knowledge import KNOWLEDGE_PROMPT
from app.ai.service import LLMService


class KnowledgeAgent:
    """
    Agent responsible for converting raw educational content
    into structured study notes.
    """

    def __init__(
        self,
        llm_service: LLMService,
    ) -> None:
        self._llm_service = llm_service

    async def generate(
        self,
        text: str,
    ) -> ChatResponse:
        """
        Generate structured knowledge notes.
        """

        prompt = KNOWLEDGE_PROMPT.invoke(
            {
                "text": text,
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
            provider=Provider.OLLAMA,
            model="gemma3:1b",
            messages=messages,
        )

        return await self._llm_service.generate(
            request
        )