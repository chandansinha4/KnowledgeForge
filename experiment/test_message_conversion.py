from app.ai.models import (
    Message,
    Role,
)
from app.ai.service import LLMService

messages = [
    Message(
        role=Role.SYSTEM,
        content="You are a helpful assistant."
    ),
    Message(
        role=Role.USER,
        content="What is LangGraph?"
    ),
]

converted = LLMService._to_langchain_messages(
    messages
)

print(type(converted))

for message in converted:
    print(type(message))
    print(message)
    print("-" * 40)