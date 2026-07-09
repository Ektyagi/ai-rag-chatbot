from collections import defaultdict

from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.services.vector_store import vector_store
from app.services.conversation_service import (
    get_history,
    add_message,
)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0,
)


def rewrite_question(history_text: str, question: str) -> str:
    """
    Rewrite follow-up questions into standalone questions
    for better vector retrieval.
    """

    if not history_text.strip():
        return question

    prompt = f"""
You are a query rewriting assistant.

Your job is to rewrite follow-up questions into standalone questions.

Conversation:

{history_text}

Latest User Question:

{question}

Instructions:
- Replace pronouns like "it", "this", "that", "they", etc.
- Preserve the original meaning.
- Do NOT answer the question.
- Return ONLY the rewritten question.

Standalone Question:
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def chat(conversation_id: str, question: str):

    # =====================================
    # Load Conversation History
    # =====================================

    history = get_history(conversation_id)

    history_text = ""

    for message in history:
        role = "User" if message["role"] == "user" else "Assistant"
        history_text += f"{role}: {message['content']}\n"

    # =====================================
    # Rewrite Follow-up Question
    # =====================================

    rewritten_question = rewrite_question(
        history_text,
        question,
    )

    print("\n==============================")
    print("Original Question:")
    print(question)

    print("\nRewritten Question:")
    print(rewritten_question)
    print("==============================")

    # =====================================
    # Retrieve Relevant Chunks
    # =====================================

    results = vector_store.similarity_search_with_score(
        query=rewritten_question,
        k=5,
    )

    if not results:

        answer = "I couldn't find any relevant information in the uploaded documents."

        add_message(
            conversation_id,
            "user",
            question,
        )

        add_message(
            conversation_id,
            "assistant",
            answer,
        )

        return {
            "answer": answer,
            "sources": [],
        }

    # =====================================
    # Build Context
    # =====================================

    context = ""

    unique_sources = defaultdict(list)

    print("\nRetrieved Chunks:\n")

    for i, (doc, score) in enumerate(results, start=1):

        print(f"Chunk {i}")
        print(f"Similarity Score: {1 - score:.2f}")
        print(f"Source: {doc.metadata.get('source')}")
        print("-" * 80)

        context += f"""
DOCUMENT CHUNK {i}

{doc.page_content}

-----------------------------------
"""

        source = doc.metadata.get("source")
        chunk = doc.metadata.get("chunk")

        if chunk is not None:
            unique_sources[source].append(chunk)

    # =====================================
    # Prompt
    # =====================================

    prompt = f"""
You are an AI RAG assistant.

Answer ONLY using the provided document context.

The conversation history is ONLY to understand follow-up questions.

Rules:

- Never use outside knowledge.
- Never invent information.
- If the answer is not in the document context, reply exactly:

"I couldn't find that information in the uploaded documents."

- Combine information from multiple chunks when needed.
- Be concise.
- Use bullet points when appropriate.
- Quote important statements exactly when helpful.

=========================
CONVERSATION HISTORY
=========================

{history_text}

=========================
DOCUMENT CONTEXT
=========================

{context}

=========================
USER QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""

    response = llm.invoke(prompt)

    answer = response.content.strip()

    # =====================================
    # Save Conversation
    # =====================================

    add_message(
        conversation_id,
        "user",
        question,
    )

    add_message(
        conversation_id,
        "assistant",
        answer,
    )

    # =====================================
    # Build Sources
    # =====================================

    sources = []

    for source, chunks in unique_sources.items():

        sources.append(
            {
                "source": source,
                "chunks": sorted(chunks),
            }
        )

    return {
        "answer": answer,
        "sources": sources,
    }