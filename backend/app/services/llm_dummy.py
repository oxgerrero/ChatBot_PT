import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.interfaces.llm_interface import LLMInterface

class DummyLLM(LLMInterface):
    def generate_answer(self, context: str, question: str) -> str:
        return f"[SIMULADO] Respondí tu pregunta '{question}' con base en el contexto local."
