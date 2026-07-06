from fastapi import APIRouter

from app.api.v1.endpoints import documents, health

router = APIRouter()
router.include_router(
    health.router,
    tags=["Health"],
)

router.include_router(
    documents.router,
    tags=["Documents"],
)