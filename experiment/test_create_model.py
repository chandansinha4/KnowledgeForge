from app.ai.models import (
    ChatRequest,
    Message,
    Provider,
)
from app.ai.service import LLMService

service = LLMService()

model = service._create_model(
    ChatRequest(
        provider=Provider.OLLAMA,
        model="gemma3:1b",
        messages=[
            Message.system("You are helpful."),
            Message.user("Hello!")
        ]
    )
)

print(type(model))
print(model)