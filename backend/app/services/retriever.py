import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pickle
from sklearn.metrics.pairwise import cosine_similarity
from openai import embeddings
from app.models.document import Document
from app.core.interfaces.retriever_interface import RetrieverInterface

class SimpleRetriever(RetrieverInterface):
    def __init__(self, path="app/data/embeddings.pkl"):
        with open(path, "rb") as f:
            self.docs_raw, self.embeddings = pickle.load(f)

    def retrieve(self, query: str, k: int = 5) -> list[Document]:
        query_embedding = embeddings.create(
            model="text-embedding-3-small",
            input=query
        ).data[0].embedding
        sims = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = sims.argsort()[-k:][::-1]
        return [Document(**self.docs_raw[i]) for i in top_indices]
