from __future__ import annotations

import asyncio

from app.ingestion.youtube import YouTubeTranscriptService


async def main() -> None:
    service = YouTubeTranscriptService()

    url = "https://www.youtube.com/watch?v=J7DzL2_Na80&t=232s"

    document = await service.ingest(url)

    print("=" * 60)
    print("TRANSCRIPT DOCUMENT")
    print("=" * 60)

    print(f"Title: {document.title}")
    print()

    print("Transcript:")
    print(document.transcript)


if __name__ == "__main__":
    asyncio.run(main())