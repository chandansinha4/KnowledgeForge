# from langchain_core.prompts import ChatPromptTemplate

# prompt=ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are an expert AI tutor"
#         ),
#         (
#             "human",
#             "{question}"
#         ),

#     ]
# )

# formatted_prompt=prompt.invoke(
#     {
#         "question":"Explain Retrieval-Augmented Generation."
#     }
# )

# print("=" * 60)
# print("TYPE")
# print("=" * 60)

# print(type(formatted_prompt))

# print()

# print("=" * 60)
# print("PROMPT")
# print("=" * 60)

# print(formatted_prompt)

# print()

# print("=" * 60)
# print("MESSAGES")
# print("=" * 60)

# for message in formatted_prompt.messages:
#     print(type(message))
#     print(message)
#     print("-" * 40)


from app.ai.prompts.knowledge import KNOWLEDGE_PROMPT

prompt = KNOWLEDGE_PROMPT.invoke(
    {
        "text": "Retrieval-Augmented Generation combines..."
    }
)

print(prompt)