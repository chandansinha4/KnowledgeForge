from __future__ import annotations

from fastapi import APIRouter

from app.api.schemas.health import HealthResponse
from app.core.config import settings
from app.health.service import HealthService

router = APIRouter(
    prefix="/api/v1/health",
    tags=["Health"],
)

health_service = HealthService(settings)


@router.get(
    "",
    response_model=HealthResponse,
    summary="Get application health status",
)
async def health() -> HealthResponse:
    """
    Return the current application health status.
    """

    status = health_service.get_status()

    return HealthResponse(
        status=status.status,
        app=status.app,
        version=status.version,
        environment=status.environment,
        provider=status.provider,
        model=status.model,
    )