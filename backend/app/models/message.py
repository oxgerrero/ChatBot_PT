from pydantic import BaseModel
from typing import List

class HistoryItem(BaseModel):
    role: str
    content: str

class Message(BaseModel):
    question: str
    session_id: str
