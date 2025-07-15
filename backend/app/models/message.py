from pydantic import BaseModel, Field
from typing import List

class HistoryItem(BaseModel):
    role: str
    content: str

class Message(BaseModel):
    question: str = Field(..., min_length=1)
    session_id: str
