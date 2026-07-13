from langchain_core.messages import AIMessage

from app.ai.service import LLMService


response = AIMessage(
    content="Hello!",
    usage_metadata={
        "input_tokens": 10,
        "output_tokens": 20,
        "total_tokens": 30,
    },
)

usage = LLMService._extract_usage(response)

print(usage)