from __future__ import annotations

from app.ai.models import (
    ChatRequest,
    Message,
    Provider,
)
from app.ai.prompts.knowledge import KNOWLEDGE_PROMPT
from app.ai.service import LLMService
from app.core.config import Settings
import re

from app.domain.knowledge import KnowledgeDocument

class KnowledgeAgent:
    """
    Agent responsible for converting raw educational content
    into structured study notes.
    """

    def __init__(
        self,
        llm_service: LLMService,
        settings: Settings,
    ) -> None:
        self._llm_service = llm_service
        self._settings = settings

    def _extract_markdown_title(self, markdown: str) -> str:
        """
        Extract the first H1 heading from a Markdown document.
        """

        match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)

        if match:
            return match.group(1).strip()

        return "Untitled Notes"

    async def generate(
        self,
        text: str,
    ) -> KnowledgeDocument:
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
            provider=Provider(
            self._settings.DEFAULT_PROVIDER
            ),
            model=self._settings.DEFAULT_MODEL,
            messages=messages,
        )

        response = await self._llm_service.generate(request)

        title = self._extract_markdown_title(response.content)

        return KnowledgeDocument(
            title=title,
            markdown=response.content,
        )