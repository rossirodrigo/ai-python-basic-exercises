import os

from dotenv import load_dotenv
from groq import Groq

from .base import LLMService


class GroqService(LLMService):
    def __init__(self, api_key=None, model="llama-3.3-70b-versatile"):
        load_dotenv()
        self.api_key = api_key or os.getenv("GROQ_API_KEY")

        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.client = Groq(api_key=self.api_key)
        self.model = model

    def chat_completion(self, messages, temperature=1.0):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error connecting to Groq: {e}")
            raise e
