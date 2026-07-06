from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import chat

router = APIRouter()


@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    return chat(request.question)