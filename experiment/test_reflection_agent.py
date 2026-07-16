from __future__ import annotations

import asyncio

from app.agents.knowledge import KnowledgeAgent
from app.agents.reflection import ReflectionAgent
from app.ai.service import LLMService
from app.core.config import settings


async def main() -> None:
    llm_service = LLMService()

    knowledge_agent = KnowledgeAgent(
        llm_service=llm_service,
        settings=settings,
    )

    reflection_agent = ReflectionAgent(
        llm_service=llm_service,
        settings=settings,
    )

    text = """
Retrieval-Augmented Generation (RAG) combines the reasoning ability of
large language models with external knowledge retrieval. Instead of
relying only on the model's internal knowledge, RAG retrieves relevant
documents from a knowledge base and uses them as additional context for
generating responses. This improves factual accuracy, reduces
hallucinations, and enables the model to answer questions about private
or frequently changing information.
"""

    knowledge_document = await knowledge_agent.generate(text)

    reflection_document = await reflection_agent.generate(
        knowledge_document
    )

    print("=" * 60)
    print("KNOWLEDGE TITLE")
    print("=" * 60)
    print(knowledge_document.title)

    print()

    print("=" * 60)
    print("REFLECTION")
    print("=" * 60)
    print(reflection_document.markdown)


if __name__ == "__main__":
    asyncio.run(main())