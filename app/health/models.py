from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class HealthStatus:
    """
    Internal health status of the application.
    """

    status: str

    app: str

    version: str

    environment: str

    provider: str

    model: str