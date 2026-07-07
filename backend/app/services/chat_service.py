from collections import defaultdict

from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.services.vector_store import vector_store


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0,
)


def chat(question: str):

    # Retrieve relevant chunks
    results = vector_store.similarity_search_with_score(
        query=question,
        k=5,
    )

    if not results:
        return {
            "answer": "I couldn't find any relevant information in the uploaded documents.",
            "sources": [],
        }

    context = ""

    # Store unique sources
    unique_sources = defaultdict(list)

    for i, (doc, score) in enumerate(results, start=1):

        context += f"""
DOCUMENT CHUNK {i}

{doc.page_content}

-----------------------------------
"""

        source = doc.metadata.get("source")
        chunk = doc.metadata.get("chunk")

        if chunk is not None:
            unique_sources[source].append(chunk)

    prompt = f"""
You are an AI assistant that answers questions ONLY using the provided context.

Instructions:

- Read every document chunk carefully.
- Use ONLY the provided context.
- Never use outside knowledge.
- If the answer cannot be found in the context, respond:
  "I couldn't find that information in the uploaded documents."
- If multiple chunks contain useful information, combine them into one answer.
- Keep the answer concise.
- Quote important statements when appropriate.

=========================
CONTEXT
=========================

{context}

=========================
QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""

    response = llm.invoke(prompt)

    sources = []

    for source, chunks in unique_sources.items():
        sources.append(
            {
                "source": source,
                "chunks": sorted(chunks),
            }
        )

    return {
        "answer": response.content,
        "sources": sources,
    }