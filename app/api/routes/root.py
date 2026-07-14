from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.
    """

    return {
        "message": "Welcome to KnowledgeForge API 🚀"
    }