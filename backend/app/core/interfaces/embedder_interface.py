from abc import ABC, abstractmethod

class EmbedderInterface(ABC):
    @abstractmethod
    def embed_text(self, text: str) -> list:
        pass
