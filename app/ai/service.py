from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    BaseMessage,
    SystemMessage,
)
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

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
    
    def _build_chat_response(
        self,
        response: AIMessage,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Convert a LangChain AIMessage into the application's ChatResponse.
        """

        return ChatResponse(
            content=response.content,
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

            return self._build_chat_response(
                response=response,
                request=request,
            )

        except Exception as exc:

            logger.exception(
                "Failed to generate LLM response."
            )

            raise LLMError(
                "Failed to generate response from the LLM."
            ) from exc