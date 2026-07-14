import asyncio

from app.agents.knowledge import KnowledgeAgent
from app.ai.service import LLMService


async def main() -> None:
    llm_service = LLMService()
    knowledge_agent = KnowledgeAgent(llm_service)

    text = """
    Retrieval-Augmented Generation (RAG) combines the reasoning ability of
    Large Language Models with external knowledge retrieval.

    Instead of relying only on the model's internal knowledge, RAG first
    retrieves relevant documents from a knowledge base and then uses those
    documents as context for generating responses.

    This approach improves factual accuracy, reduces hallucinations,
    and allows LLMs to answer questions about private or frequently
    changing data.
    """

    response = await knowledge_agent.generate(text)

    print("=" * 60)
    print("KNOWLEDGE AGENT RESPONSE")
    print("=" * 60)

    print(response.content)

    print()

    print("=" * 60)
    print("TOKEN USAGE")
    print("=" * 60)

    print(response.usage)

    print()

    print("=" * 60)
    print("METADATA")
    print("=" * 60)

    print(response.response_metadata)


if __name__ == "__main__":
    asyncio.run(main())