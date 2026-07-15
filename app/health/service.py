from __future__ import annotations

from app.core.config import Settings
from app.health.models import HealthStatus


class HealthService:
    """
    Service responsible for reporting the application's health status.
    """

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def get_status(self) -> HealthStatus:
        """
        Return the current application health status.
        """

        return HealthStatus(
            status="healthy",
            app=self._settings.APP_NAME,
            version=self._settings.APP_VERSION,
            environment=self._settings.APP_ENV,
            provider=self._settings.DEFAULT_PROVIDER,
            model=self._settings.DEFAULT_MODEL,
        )