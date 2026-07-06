from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.services.vector_store import vector_store


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0,
)


def chat(question: str):

    # Retrieve the most relevant chunks
    results = vector_store.similarity_search_with_score(
        query=question,
        k=5,
    )

    # If nothing is found
    if not results:
        return {
            "answer": "I couldn't find any relevant information in the uploaded documents.",
            "sources": []
        }

    # Build the context
    context = "\n\n".join(
        doc.page_content
        for doc, score in results
    )

    # Prompt
    prompt = f"""
You are an AI assistant.

Use ONLY the provided context to answer the user's question.

Rules:
- Never use outside knowledge.
- If the answer is not present in the context, respond:
  "I couldn't find that information in the uploaded documents."
- Keep the answer concise.
- Quote important information exactly when possible.

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate response
    response = llm.invoke(prompt)

    # Prepare sources
    sources = []

    for doc, score in results:
        sources.append(
            {
                "source": doc.metadata.get("source"),
                "chunk": doc.metadata.get("chunk"),
                "distance": round(score, 4),
            }
        )

    return {
        "answer": response.content,
        "sources": sources,
    }