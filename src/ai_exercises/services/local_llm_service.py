import os

import dirtyjson
from dotenv import load_dotenv
from openai import OpenAI

from .base import LLMService

load_dotenv()


class LocalLLMService(LLMService):
    def __init__(
        self,
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
        model="google/gemma-3n-e4b:2",
    ):
        self.client = OpenAI(
            base_url=base_url, api_key=api_key or os.getenv("LOCAL_LLM_API_KEY")
        )
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
            print(f"Error connecting to local LLM: {e}")
            raise e

    def _parse_json(self, text):
        # Local models are less reliable at strict JSON, so use a tolerant parser.
        return dirtyjson.loads(text.replace("\\", "\\\\"))
