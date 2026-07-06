import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY FOUND:", bool(api_key))
print(api_key[:10] + "..." if api_key else "NO KEY")

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=api_key,
)

try:
    result = embeddings.embed_query("Hello World")
    print("SUCCESS")
    print(len(result))
except Exception as e:
    print(type(e))
    print(e)