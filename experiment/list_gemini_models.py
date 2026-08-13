from google import genai

from app.core.config import settings


def main() -> None:
    client = genai.Client(
        api_key=settings.GEMINI_API_KEY,
    )

    for model in client.models.list():
        print(model.name)


if __name__ == "__main__":
    main()