import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()


class GeminiService:
    def __init__(self, api_key=None, model="gemini-flash-lite-latest"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def generate_json(self, prompt, data):
        """
        Sends a prompt and data to Gemini and returns a parsed JSON response.
        """
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=f"""
                    {prompt}
                    
                    STRICT RULES:
                    1. Return ONLY the valid JSON. No conversational text or markdown code blocks.
                    2. Ensure the output is a valid JSON.

                    Payload to process:
                    {json.dumps(data)}
                """,
            )

            # Clean markdown and whitespace from the response
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_text)

        except Exception as e:
            print(f"Error connecting to Gemini: {e}")
            raise e
