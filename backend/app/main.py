from fastapi import FastAPI

app = FastAPI(
    title="AI RAG Chatbot API",
    description="Backend API for the AI-powered chatbot",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the AI RAG Chatbot!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    } 