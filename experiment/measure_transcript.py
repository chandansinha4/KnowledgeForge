from __future__ import annotations

import asyncio

from app.ingestion.youtube import YouTubeTranscriptService


def estimate_tokens(text: str) -> int:
    """
    Estimate token count from transcript text.

    This is only used for pre-processing decisions.
    Actual LLM token usage remains the authoritative measurement.
    """
    TOKENS_PER_WORD_ESTIMATE = 1.3

    word_count = len(text.split())

    return int(word_count * TOKENS_PER_WORD_ESTIMATE)


async def main() -> None:
    url = input("Enter YouTube URL: ").strip()

    service = YouTubeTranscriptService()

    transcript_document = await service.ingest(url)

    transcript = transcript_document.transcript

    character_count = len(transcript)
    word_count = len(transcript.split())
    estimated_tokens = estimate_tokens(transcript)

    print("=" * 60)
    print("TRANSCRIPT MEASUREMENTS")
    print("=" * 60)

    print(f"Characters       : {character_count:,}")
    print(f"Words            : {word_count:,}")
    print(f"Estimated tokens : {estimated_tokens:,}")


if __name__ == "__main__":
    asyncio.run(main())