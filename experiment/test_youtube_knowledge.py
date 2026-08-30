from app.agents.knowledge import KnowledgeAgent
from app.agents.reflection import ReflectionAgent
from app.ai.service import LLMService
from app.core.config import settings
from app.ingestion.youtube import YouTubeTranscriptService
from app.workflow.youtube_learning import YouTubeLearningWorkflow

async def main() -> None:
    url = input("Enter YouTube URL: ").strip()

    transcript_service = YouTubeTranscriptService()
    llm_service = LLMService()

    knowledge_agent = KnowledgeAgent(
    llm_service=llm_service,
    settings=settings,
)

    reflection_agent = ReflectionAgent(
        llm_service=llm_service,
        settings=settings,
    )

    workflow = YouTubeLearningWorkflow(
    transcript_service=transcript_service,
    knowledge_agent=knowledge_agent,
    reflection_agent=reflection_agent,
    )

    result = await workflow.run(url)

    print("\n" + "=" * 60)
    print("KNOWLEDGE DOCUMENT")
    print("=" * 60)

    print(f"\nTitle: {result.knowledge.title}\n")
    #print(result.knowledge.markdown)

    print("\nKNOWLEDGE LENGTH")
    print("Characters:", len(result.knowledge.markdown))
    print("Words:", len(result.knowledge.markdown.split()))
    print("Preview:")
    print(result.knowledge.markdown[:500])

    print("\n" + "=" * 60)
    print("REFLECTION DOCUMENT")
    print("=" * 60)

    print(result.reflection.markdown)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())