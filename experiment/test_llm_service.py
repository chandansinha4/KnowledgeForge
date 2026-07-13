import asyncio

from app.ai.models import (
    ChatRequest,
    Message,
    Provider,
)
from app.ai.service import LLMService


async def main() -> None:
    service = LLMService()

    request = ChatRequest(
        provider=Provider.OLLAMA,
        model="gemma3:1b",
        messages=[
            Message.system(
                "You are a test assistant. Follow the user's instructions exactly and do not add extra words."
            ),
            Message.user(
                "Reply with exactly: Hello World"
            ),
        ],
    )

    response = await service.generate(request)

    print("=" * 60)
    print("CHAT RESPONSE")
    print("=" * 60)

    print(response)

    print()

    print("=" * 60)
    print("CONTENT")
    print("=" * 60)

    print(response.content)

    print()

    print("=" * 60)
    print("TOKEN USAGE")
    print("=" * 60)

    print(response.usage)

    print()

    print("=" * 60)
    print("RESPONSE METADATA")
    print("=" * 60)

    print(response.response_metadata)


if __name__ == "__main__":
    asyncio.run(main())