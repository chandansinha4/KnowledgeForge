from langchain_core.messages import AIMessage

from app.ai.models import (
    ChatRequest,
    Message,
    Provider,
)
from app.ai.service import LLMService


service = LLMService()

response = AIMessage(
    content="Hello!",
    response_metadata={
        "model": "gemma3:1b"
    },
    usage_metadata={
        "input_tokens": 10,
        "output_tokens": 20,
        "total_tokens": 30,
    },
)

request = ChatRequest(
    provider=Provider.OLLAMA,
    model="gemma3:1b",
    messages=[
        Message.system("You are helpful."),
        Message.user("Hello"),
    ],
)

chat_response = service._build_chat_response(
    response=response,
    request=request,
)

print(chat_response)