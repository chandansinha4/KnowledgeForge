from __future__ import annotations

import asyncio

from app.agents.knowledge import KnowledgeAgent
from app.ai.service import LLMService
from app.core.config import settings
from app.ingestion.youtube import YouTubeTranscriptService


async def main() -> None:
    youtube_service = YouTubeTranscriptService()

    llm_service = LLMService()

    knowledge_agent = KnowledgeAgent(
        llm_service=llm_service,
        settings=settings,
    )

    url = "https://www.youtube.com/watch?v=lvO88XxNAzs"

    # Step 1: Ingest YouTube transcript
    transcript_document = await youtube_service.ingest(url)

    print("=" * 60)
    print("TRANSCRIPT")
    # print("=" * 60)
    # print(transcript_document.transcript)

    with open("t8_transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript_document.transcript)

    print("Transcript saved.")
    print(f"Characters: {len(transcript_document.transcript):,}")
    print(f"Words: {len(transcript_document.transcript.split()):,}")

    # Step 2: Generate knowledge from transcript
    knowledge_document = await knowledge_agent.generate(
        transcript_document.transcript,
    )

    print()
    print("=" * 60)
    print("KNOWLEDGE DOCUMENT")
    print("=" * 60)
    print()

    print(f"Title: {knowledge_document.title}")
    print()
    print(knowledge_document.markdown)


if __name__ == "__main__":
    asyncio.run(main())