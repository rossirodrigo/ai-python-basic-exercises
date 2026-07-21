import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from .base import LLMService

_ROLE_MAP = {"assistant": "model", "user": "user"}


class GeminiService(LLMService):
    def __init__(self, api_key=None, model="gemini-flash-lite-latest"):
        load_dotenv()
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def chat_completion(self, messages, temperature=1.0):
        system_instruction = "\n".join(
            message["content"] for message in messages if message["role"] == "system"
        )
        contents = [
            {
                "role": _ROLE_MAP[message["role"]],
                "parts": [{"text": message["content"]}],
            }
            for message in messages
            if message["role"] != "system"
        ]

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction or None,
                    temperature=temperature,
                ),
            )
            return response.text
        except Exception as e:
            print(f"Error connecting to Gemini: {e}")
            raise e
