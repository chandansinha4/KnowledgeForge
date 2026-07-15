# KnowledgeForge Architecture

## Overview

KnowledgeForge is an AI-powered learning assistant that transforms long-form educational content into structured, reusable knowledge.

The project is designed around a layered architecture that separates HTTP concerns, business logic, prompt engineering, AI orchestration, and content export. This separation keeps the system modular, testable, and easy to extend as new capabilities are introduced.

The long-term goal is to create an AI system that helps users learn from educational content and seamlessly integrates the generated knowledge into their personal knowledge management workflow.

---

# Design Principles

KnowledgeForge is built around the following engineering principles:

* Separation of concerns
* Single Responsibility Principle (SRP)
* Dependency Injection
* Provider-agnostic AI integration
* Centralized configuration
* Domain-driven design
* Incremental architecture evolution
* Explicit domain models
* Consistent request flow

Every new feature should follow these principles.

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

# Current Request Flow

Every AI request follows the same pipeline.

```text
HTTP Request
      │
      ▼
API Route
      │
      ▼
Request Schema
      │
      ▼
Agent
      │
      ▼
Prompt Template
      │
      ▼
LLM Service
      │
      ▼
LangChain
      │
      ▼
LLM Provider
      │
      ▼
Domain Object
      │
      ▼
Response Schema
      │
      ▼
HTTP Response
```

This keeps HTTP, business logic, prompts, and AI infrastructure completely independent.

---

# Layer Responsibilities

## API Layer

Responsible for:

* Exposing REST endpoints
* Request validation
* Response serialization
* Swagger documentation

The API layer never communicates directly with language models.

---

## Agent Layer

Agents represent AI capabilities.

Examples include:

* KnowledgeAgent
* ReflectionAgent

Future agents:

* QuizAgent
* FlashcardAgent

Each agent is responsible for:

* Selecting the correct prompt
* Preparing prompt variables
* Calling the LLM service
* Returning domain objects

Agents never contain HTTP logic.

---

## Service Layer

Services provide reusable business functionality that is not tied to a specific AI capability.

Current services include:

* HealthService
* LLMService

Future services may include:

* TranscriptService
* ExportService

---

## Prompt Layer

Each AI capability owns its own prompt.

Examples:

* Knowledge Prompt
* Reflection Prompt

Future prompts:

* Quiz Prompt
* Flashcard Prompt

Prompt engineering is isolated from application logic.

---

## LLM Service

The LLMService acts as the provider abstraction layer.

Responsibilities:

* Model creation
* Provider selection
* Request execution
* Token usage extraction
* Response metadata extraction

The rest of the application never depends directly on LangChain or specific LLM providers.

---

## Domain Models

KnowledgeForge exchanges structured domain objects instead of raw strings.

Examples:

* HealthStatus
* KnowledgeDocument
* ReflectionDocument

Domain models become the common language between different components of the system.

---

## Configuration

Application configuration is centralized using Pydantic Settings.

Configuration is loaded once during application startup from the `.env` file.

Configuration includes:

* Default provider
* Default model
* Temperature
* Maximum tokens
* Top-p
* API keys
* Logging configuration

No agent or service hardcodes provider-specific values.

---

# Version 1 Workflow

The first complete workflow of KnowledgeForge is focused on learning from YouTube videos.

```text
                 YouTube URL
                      │
                      ▼
           Transcript Extraction
                      │
                      ▼
            Transcript Cleaning
                      │
                      ▼
             Knowledge Agent
                      │
                      ▼
           KnowledgeDocument
                      │
                      ▼
             Reflection Agent
                      │
                      ▼
          ReflectionDocument
                      │
                      ▼
                 Export Layer
          ┌─────────┼──────────┐
          ▼         ▼          ▼
      Markdown   Obsidian    Notion
```

This represents the complete Version 1 user workflow.

---

# Project Structure

```text
app/
│
├── agents/
│   ├── knowledge.py
│   └── reflection.py
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
├── exporters/
│
├── youtube/
│
└── main.py
```

Some directories represent future milestones and may not yet exist.

---

# Roadmap

## Version 1.0

Goal:

Transform a YouTube video into structured learning notes.

Includes:

* Transcript extraction
* Knowledge generation
* Reflection generation
* Markdown export

---

## Version 1.1

Improve integration with knowledge management systems.

Includes:

* Obsidian export
* Notion export
* PDF export

---

## Version 1.2

Learning enhancement features.

Includes:

* Quiz generation
* Flashcard generation
* Anki export

---

## Version 2.0

Advanced AI orchestration.

Includes:

* LangGraph workflow
* PDF ingestion
* Retrieval-Augmented Generation (RAG)
* Multi-source knowledge processing
* Semantic search

---

# Architectural Philosophy

KnowledgeForge is built by first establishing a stable foundation and then layering new capabilities on top of it.

Instead of continuously redesigning the system, new features are added through composition.

This approach keeps the architecture predictable, scalable, and easy to maintain while allowing the project to evolve from a simple AI application into a complete AI-powered learning platform.
