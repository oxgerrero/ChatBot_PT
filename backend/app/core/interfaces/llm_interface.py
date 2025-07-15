from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def generate_answer(self, context: str, question: str) -> str:
        pass
