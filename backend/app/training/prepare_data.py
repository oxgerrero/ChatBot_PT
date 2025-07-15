import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import pickle
import openai
import os
from app.core.config import settings
import textwrap

openai.api_key = settings.OPENAI_API_KEY

MAX_CHARS = 20000  # Aproximadamente 8000 tokens (límite modelo embedding)

# Truncado seguro (opción por defecto)
def safe_truncate(text: str, max_chars: int = MAX_CHARS) -> str:
    return text[:max_chars]

# Chunking alternativo (opcional)
def chunk_text(text: str, chunk_size: int = 2000) -> list:
    return textwrap.wrap(text, width=chunk_size)

def prepare_embeddings():
    df = pd.read_csv("app/data/documents.csv")
    documents = []
    embeddings = []

    for row in df.itertuples():
        full_text = f"{row.title}\n{row.text}"

        chunks = chunk_text(full_text)
        for i, chunk in enumerate(chunks):
            chunk_id = f"{row.doc_id}_chunk{i}"
            embedding = openai.embeddings.create(
                model=settings.EMBEDDING_MODEL,
                input=chunk
            ).data[0].embedding
            documents.append({"id": chunk_id, "text": chunk})
            embeddings.append(embedding)

    os.makedirs("app/data", exist_ok=True)
    with open("app/data/embeddings.pkl", "wb") as f:
        pickle.dump((documents, embeddings), f)

    print(f"✅ Embeddings generados para {len(documents)} documentos.")

if __name__ == "__main__":
    prepare_embeddings()
