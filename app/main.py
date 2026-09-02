from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.root import router as root_router
from app.api.routes.knowledge import router as knowledge_router
from app.api.routes.health import router as health_router
from app.api.routes.reflection import router as reflection_router
from app.api.routes.youtube import router as youtube_router


app = FastAPI(
    title="KnowledgeForge API",
    description=(
        "AI-powered knowledge management system "
        "that transforms YouTube videos into structured notes."
    ),
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(root_router)
app.include_router(knowledge_router)
app.include_router(health_router)
app.include_router(reflection_router)
app.include_router(youtube_router)