from fastapi import APIRouter
from app.ai.service import LLMService

from app.ai.models import (
    ChatRequest,
    Message,
)
from app.api.schemas import (
    ChatAPIRequest,
    ChatAPIResponse,
)

llm_service = LLMService()

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"],
)

@router.post(
    "",
    response_model=ChatAPIResponse,
)
async def chat(
    request: ChatAPIRequest,
) -> ChatAPIResponse:
    
    chat_request = ChatRequest(
    provider=request.provider,
    model=request.model,
    messages=[
        Message.system(
            "You are a helpful AI assistant."
        ),
        Message.user(
            request.prompt
        ),
        ],
    )

    response = await llm_service.generate(
    chat_request
    )

    return ChatAPIResponse(
    content=response.content,
    provider=response.provider,
    model=response.model,
    input_tokens=(
        response.usage.input_tokens
        if response.usage
        else None
    ),
    output_tokens=(
        response.usage.output_tokens
        if response.usage
        else None
    ),
    total_tokens=(
        response.usage.total_tokens
        if response.usage
        else None
    ),
    )