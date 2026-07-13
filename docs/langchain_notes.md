# Experiment 1 - ChatPromptTemplate

## Findings

- ChatPromptTemplate is not sent directly to the LLM.
- invoke() returns a ChatPromptValue.
- ChatPromptValue contains a list of LangChain messages.
- Messages are automatically converted to SystemMessage and HumanMessage.
- Variable substitution happens during invoke().

# Experiment 2 - Prompt Templates

## Findings

- ChatPromptTemplate.invoke() returns ChatPromptValue.
- ChatPromptValue contains LangChain messages.
- Variable substitution happens during invoke().

---

# Experiment 3 - LLM Response

## Findings

- ChatOllama returns AIMessage.
- AIMessage contains:
  - content
  - usage_metadata
  - response_metadata
  - tool_calls
- Token usage is available through usage_metadata.
- response_metadata contains provider-specific information.