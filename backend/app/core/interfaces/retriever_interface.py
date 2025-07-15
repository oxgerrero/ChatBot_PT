import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from typing import List
from app.models.document import Document

class RetrieverInterface(ABC):
    @abstractmethod
    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        pass
