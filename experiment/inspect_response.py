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

chain = prompt | llm

response = chain.invoke(
    {
        "question": "Explain Retrieval-Augmented Generation in one paragraph."
    }
)

print("=" * 60)
print("TYPE")
print("=" * 60)
print(type(response))

print()

print("=" * 60)
print("FULL RESPONSE")
print("=" * 60)
print(response)

print()

print("=" * 60)
print("CONTENT")
print("=" * 60)
print(response.content)

print()

print("=" * 60)
print("RESPONSE METADATA")
print("=" * 60)
print(response.response_metadata)

print()

print("=" * 60)
print("USAGE METADATA")
print("=" * 60)
print(response.usage_metadata)

print()

print("=" * 60)
print("ID")
print("=" * 60)
print(response.id)

print()

print("=" * 60)
print("ALL ATTRIBUTES")
print("=" * 60)

for attr in dir(response):
    if not attr.startswith("_"):
        print(attr)