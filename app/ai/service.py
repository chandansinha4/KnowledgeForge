from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    BaseMessage,
    SystemMessage,
)
from langchain_ollama import ChatOllama

from app.ai.models import (
    ChatRequest,
    ChatResponse,
    Message,
    Provider,
    Role,
    TokenUsage,
)
from app.core.config import get_settings
from app.core.exceptions import LLMError
from app.core.logger import logger
from langchain_google_genai import ChatGoogleGenerativeAI


class LLMService:
    """
    Service responsible for all communication with LLM providers.

    Responsibilities:
    - Create the appropriate LangChain chat model
    - Convert application messages to LangChain messages
    - Invoke the model
    - Convert LangChain responses to application responses
    """

    def __init__(self) -> None:
        self.settings = get_settings()
    
    def _create_model(
    self,
    request: ChatRequest,
    ) -> BaseChatModel:
        
        """Create and return the appropriate LangChain chat model."""

        config = request.generation_config

        temperature = (
            config.temperature
            if config and config.temperature is not None
            else self.settings.DEFAULT_TEMPERATURE
        )

        max_tokens = (
            config.max_tokens
            if config and config.max_tokens is not None
            else self.settings.DEFAULT_MAX_TOKENS
        )

        top_p = (
            config.top_p
            if config and config.top_p is not None
            else self.settings.DEFAULT_TOP_P
        )

        match request.provider:

            case Provider.OLLAMA:
                return ChatOllama(
                    model=request.model,
                    temperature=temperature,
                    num_predict=max_tokens,
                    top_p=top_p,
                    base_url=self.settings.OLLAMA_BASE_URL,
                )

            case Provider.GEMINI:
                return ChatGoogleGenerativeAI(
                    model=request.model,
                    google_api_key=self.settings.GEMINI_API_KEY,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p,
                )

            case _:
                raise LLMError(
                f"Provider '{request.provider.value}' is not supported yet."
            )
    
    @staticmethod
    def _to_langchain_messages(
        messages: list[Message],
    ) -> list[BaseMessage]:
        """
        Convert application messages into LangChain messages.
        """

        langchain_messages: list[BaseMessage] = []

        for message in messages:

            match message.role:

                case Role.SYSTEM:
                    langchain_messages.append(
                        SystemMessage(
                            content=message.content,
                        )
                    )

                case Role.USER:
                    langchain_messages.append(
                        HumanMessage(
                            content=message.content,
                        )
                    )

                case Role.ASSISTANT:
                    langchain_messages.append(
                        AIMessage(
                            content=message.content,
                        )
                    )

                case _:
                    raise LLMError(
                        f"Unsupported message role: {message.role}"
                    )

        return langchain_messages
    
    @staticmethod
    def _extract_usage(
        response: AIMessage,
    ) -> TokenUsage | None:
        """
        Extract token usage information from a LangChain AIMessage.
        """

        usage = response.usage_metadata

        if usage is None:
            return None

        return TokenUsage(
            input_tokens=usage.get("input_tokens"),
            output_tokens=usage.get("output_tokens"),
            total_tokens=usage.get("total_tokens"),
        )
    @staticmethod
    def _extract_content(
        response: AIMessage,
    ) -> str:
        """
        Extract text content from a LangChain AIMessage.

        Different LLM providers may return content in
        different representations. Normalize them into
        a plain string for the application layer.
        """

        content = response.content

        if isinstance(content, str):
            return content

        if isinstance(content, list):
            text_parts: list[str] = []

            for block in content:
                if isinstance(block, dict):
                    text = block.get("text")

                    if isinstance(text, str):
                        text_parts.append(text)

            return "".join(text_parts)

        raise LLMError(
            f"Unsupported response content type: {type(content).__name__}"
        )

    
    def _build_chat_response(
        self,
        response: AIMessage,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Convert a LangChain AIMessage into the application's ChatResponse.
        """

        return ChatResponse(
        content=self._extract_content(response),
        provider=request.provider,
        model=request.model,
        usage=self._extract_usage(response),
        response_metadata=response.response_metadata,
    )
    
    async def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Generate a response from the configured LLM provider.
        """

        logger.info(
            "Generating response using provider=%s model=%s",
            request.provider.value,
            request.model,
        )

        try:
            model = self._create_model(request)

            messages = self._to_langchain_messages(
                request.messages
            )

            response = await model.ainvoke(messages)

            chat_response = self._build_chat_response(
                response=response,
                request=request,
            )
            logger.info(
                "LLM usage: provider=%s model=%s "
                "input_tokens=%s output_tokens=%s total_tokens=%s",
                request.provider.value,
                request.model,
                chat_response.usage.input_tokens if chat_response.usage else None,
                chat_response.usage.output_tokens if chat_response.usage else None,
                chat_response.usage.total_tokens if chat_response.usage else None,
            )
            
            return chat_response

        except Exception as exc:

            logger.exception(
                "Failed to generate LLM response."
            )

            raise LLMError(
                "Failed to generate response from the LLM."
            ) from exc