from fastapi import FastAPI

from app.api.routes.root import router as root_router
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="KnowledgeForge API",
    description=(
        "AI-powered knowledge management system "
        "that transforms YouTube videos into structured notes."
    ),
    version="0.1.0",
)

app.include_router(root_router)
app.include_router(chat_router)