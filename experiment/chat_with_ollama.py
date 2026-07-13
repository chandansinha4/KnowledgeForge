from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.2,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert AI tutor."
        ),
        (
            "human",
            "{question}"
        ),
    ]
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke(
    {
        "question": "Explain Retrieval-Augmented Generation in simple terms."
    }
)

print(response)