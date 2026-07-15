# ADR-001: Use the Agent Pattern

## Status

Accepted

---

## Context

The project requires multiple AI capabilities such as knowledge extraction, reflection generation, quizzes, and flashcards.

Embedding all prompt engineering and LLM calls directly inside API routes would tightly couple business logic with HTTP concerns and make the system difficult to maintain.

---

## Decision

Each AI capability will be implemented as an independent Agent.

Examples:

* KnowledgeAgent
* ReflectionAgent
* QuizAgent
* FlashcardsAgent

Each agent owns:

* Business logic
* Prompt selection
* Prompt variable preparation
* LLM invocation

API routes remain thin and only coordinate requests and responses.

---

## Alternatives Considered

### Direct LLM calls from API routes

Pros:

* Simpler initially

Cons:

* Poor separation of concerns
* Difficult testing
* Code duplication
* Harder to extend

---

## Consequences

Benefits:

* Clear ownership of AI capabilities
* Easier testing
* Better maintainability
* Reusable business logic

Trade-offs:

* Slightly more project structure
* Additional files for each capability
