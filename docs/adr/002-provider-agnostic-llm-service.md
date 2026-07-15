# ADR-002: Introduce a Provider-Agnostic LLM Service

## Status

Accepted

---

## Context

KnowledgeForge should support multiple LLM providers without requiring changes throughout the application.

Directly coupling agents to LangChain or a specific provider would make future migrations difficult.

---

## Decision

Introduce a dedicated LLMService responsible for:

* Creating provider-specific models
* Sending requests
* Returning standardized responses
* Extracting usage information
* Hiding LangChain implementation details

Agents communicate only with LLMService.

---

## Alternatives Considered

### Agents directly instantiate LangChain models

Pros:

* Fewer classes

Cons:

* Tight coupling
* Code duplication
* Difficult provider switching

---

## Consequences

Benefits:

* Single integration point
* Easier provider migration
* Better testing
* Cleaner architecture

Trade-offs:

* One additional abstraction layer
