import os
import json
from google import genai
from dotenv import load_dotenv


class GeminiService:
    def __init__(self, api_key=None, model="gemini-flash-lite-latest"):
        load_dotenv()
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def create_chat(self):
        return self.client.chats.create(model=self.model)

    def send_message(self, prompt, chat=None):
        try:
            if chat:
                response = chat.send_message(prompt)
            else:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                )
            return response
        except Exception as e:
            print(f"Error connecting to Gemini: {e}")
            raise e

    def generate_json(self, prompt, data):
        try:
            response = self.send_message(
                f"""
                    {prompt}

                    STRICT RULES:
                    1. Return ONLY the valid JSON. No conversational text or markdown code blocks.
                    2. Ensure the output is a valid JSON.

                    Payload to process:
                    {json.dumps(data)}
                """,
            )

            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_text)

        except Exception as e:
            raise e
