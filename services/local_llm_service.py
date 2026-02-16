import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class LocalLLMService:
    def __init__(
        self,
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
        model="google/gemma-3n-e4b",
    ):
        self.client = OpenAI(
            base_url=base_url, api_key=api_key or os.getenv("LOCAL_LLM_API_KEY")
        )
        self.model = model

    def chat_completion(self, messages, temperature=1.0):
        """
        Sends a chat completion request to the local LLM.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
            )
            return response
        except Exception as e:
            print(f"Error connecting to local LLM: {e}")
            raise e
