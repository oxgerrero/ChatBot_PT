from pydantic import BaseModel

class Document(BaseModel):
    id: str
    text: str
