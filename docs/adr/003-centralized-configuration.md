# ADR-003: Centralize AI Configuration

## Status

Accepted

---

## Context

Earlier versions of the project hardcoded provider and model names inside agents.

This made switching models require source code changes.

---

## Decision

Centralize all application and AI configuration using Pydantic Settings.

Configuration is loaded from the `.env` file during application startup and injected into services and agents as dependencies.

Examples include:

* Default provider
* Default model
* Temperature
* Top-p
* Maximum tokens
* API keys

---

## Alternatives Considered

### Hardcoded configuration inside agents

Pros:

* Simple to implement

Cons:

* Difficult to maintain
* Poor deployment flexibility
* Code changes required for configuration updates

---

## Consequences

Benefits:

* Environment-specific configuration
* Easier deployment
* Cleaner separation between code and configuration
* Improved testability through dependency injection

Trade-offs:

* Requires a valid `.env` file
* Slightly more setup for new contributors
