# KnowledgeForge Architecture

## Overview

KnowledgeForge is an AI-powered knowledge processing system designed with a layered architecture. The project focuses on maintainability, extensibility, and clear separation of concerns. Instead of exposing a generic chatbot, the application provides domain-specific AI capabilities such as knowledge extraction, reflection generation, quizzes, and flashcards.

The architecture separates HTTP concerns, business logic, prompt engineering, and LLM integration into independent layers.

---

# High-Level Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ▼
API Routes
   │
   ▼
API Schemas
   │
   ▼
Agents / Services
   │
   ▼
Prompt Templates
   │
   ▼
LLM Service
   │
   ▼
LangChain
   │
   ▼
LLM Provider
```

---

# Layer Responsibilities

## API Layer

Responsible for:

* Exposing REST endpoints
* Request validation
* Response serialization
* Converting API models to domain models

The API layer never communicates directly with an LLM.

---

## Agent Layer

Agents represent business capabilities.

Examples:

* KnowledgeAgent
* ReflectionAgent
* QuizAgent
* FlashcardsAgent

An agent is responsible for:

* Selecting the correct prompt
* Preparing input variables
* Calling the LLM service
* Returning domain objects

Agents should not contain HTTP or infrastructure logic.

---

## Prompt Layer

Prompt templates define the behavior of each AI capability.

Each agent owns its own prompt.

Current prompts include:

* Knowledge Prompt

Future prompts include:

* Reflection Prompt
* Quiz Prompt
* Flashcard Prompt

Prompt engineering is isolated from application logic.

---

## LLM Service

The LLM service provides a provider-agnostic interface for interacting with language models.

Responsibilities:

* Model creation
* Provider abstraction
* Request execution
* Token usage extraction
* Metadata extraction

The rest of the application does not depend on LangChain or specific providers.

---

## Configuration

Application configuration is centralized using Pydantic Settings.

Configuration values are loaded from the `.env` file during application startup.

Examples:

* Default provider
* Default model
* Temperature
* Top-p
* Maximum tokens
* API keys

No agent or service hardcodes model information.

---

# Current Request Flow

Knowledge generation follows this flow:

```text
HTTP Request
      │
      ▼
Knowledge Route
      │
      ▼
KnowledgeRequest
      │
      ▼
KnowledgeAgent
      │
      ▼
Knowledge Prompt
      │
      ▼
LLMService
      │
      ▼
LangChain
      │
      ▼
LLM Provider
      │
      ▼
ChatResponse
      │
      ▼
KnowledgeResponse
      │
      ▼
HTTP Response
```

---

# Design Principles

The project follows the following engineering principles:

* Separation of concerns
* Single responsibility principle
* Dependency injection
* Provider-agnostic AI integration
* Centralized configuration
* Incremental architecture evolution
* Explicit domain models
* Clear API boundaries

---

# Current Project Structure

```text
app/
│
├── agents/
│
├── ai/
│   ├── prompts/
│   ├── models.py
│   └── service.py
│
├── api/
│   ├── routes/
│   └── schemas/
│
├── core/
│
├── health/
│
└── main.py
```

---

# Future Architecture

Planned additions include:

* Reflection Agent
* Quiz Agent
* Flashcards Agent
* YouTube ingestion pipeline
* Markdown exporter
* LangGraph workflow orchestration
* Retrieval-Augmented Generation (RAG)

These capabilities will be added without changing the existing architecture, allowing the system to grow through composition rather than redesign.
