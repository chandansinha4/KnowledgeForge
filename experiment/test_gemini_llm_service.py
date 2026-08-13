from __future__ import annotations

import asyncio

from app.ai.models import ChatRequest, Message, Provider
from app.ai.service import LLMService
from app.core.config import settings


async def main() -> None:
    service = LLMService()

    request = ChatRequest(
        provider=Provider.GEMINI,
        model=settings.GEMINI_MODEL,
        messages=[
            Message.system(
                "You are a helpful educational assistant."
            ),
            Message.user(
                "Explain what linear algebra is in two sentences."
            ),
        ],
    )

    response = await service.generate(request)

    print("=" * 60)
    print("GEMINI LLM SERVICE RESPONSE")
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