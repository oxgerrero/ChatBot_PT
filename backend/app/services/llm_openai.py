import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openai
from app.core.config import settings
from app.core.interfaces.llm_interface import LLMInterface

openai.api_key = settings.OPENAI_API_KEY

class OpenAILLM(LLMInterface):
    def generate_answer(self, context: str, question: str) -> str:
        messages = [
            {"role": "system", "content": "Responde solo con base en el contexto proporcionado."},
            {"role": "user", "content": f"Contexto:\n{context}\n\nPregunta: {question}"}
        ]
        response = openai.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=messages
        )
        return response.choices[0].message.content
