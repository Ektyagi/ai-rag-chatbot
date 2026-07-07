from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.api.v1.endpoints import chat

app = FastAPI(
    title="AI RAG Chatbot",
    version="1.0.0",
)

# -------------------------
# CORS
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routes
# -------------------------
app.include_router(api_router)

app.include_router(
    chat.router,
    prefix="/v1",
    tags=["Chat"],
)

@app.get("/")
async def root():
    return {
        "message": "AI RAG Chatbot API"
    }