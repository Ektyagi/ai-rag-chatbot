from fastapi import FastAPI
from app.api.v1.endpoints import chat
from app.api.router import api_router

app = FastAPI(
    title="AI RAG Chatbot",
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": "AI RAG Chatbot API"
    }

app.include_router(
    chat.router,
    prefix="/v1",
    tags=["Chat"]
)