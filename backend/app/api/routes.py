import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter
from app.models.message import Message, HistoryItem
from app.services.llm_openai import OpenAILLM
from app.services.llm_dummy import DummyLLM
from app.services.retriever import SimpleRetriever
from app.services.chat_memory_redis import ChatMemoryRedis
from app.core.config import settings

router = APIRouter()
llm = DummyLLM() if settings.MODE == "offline" else OpenAILLM()
retriever = SimpleRetriever()
memory = ChatMemoryRedis()

@router.post("/answer")
def get_answer(msg: Message):
    history = memory.get_history(msg.session_id)
    docs = retriever.retrieve(msg.question)
    doc_context = "\n\n".join(doc.text for doc in docs)
    chat_context = "\n".join(f"{h.role}: {h.content}" for h in history)
    full_context = f"{doc_context}\n\n{chat_context}"

    answer = llm.generate_answer(full_context, msg.question)

    memory.append(msg.session_id, HistoryItem(role="user", content=msg.question))
    memory.append(msg.session_id, HistoryItem(role="assistant", content=answer))

    return {
        "answer": answer,
        "sources": [doc.id for doc in docs]
    }
