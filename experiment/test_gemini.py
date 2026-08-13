from __future__ import annotations

from google import genai

from app.core.config import settings


def main() -> None:
    client = genai.Client(
        api_key=settings.GEMINI_API_KEY,
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain linear algebra in two sentences.",
    )

    print("=" * 60)
    print("GEMINI RESPONSE")
    print("=" * 60)
    print(response.text)


if __name__ == "__main__":
    main()