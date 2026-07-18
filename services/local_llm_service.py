import dirtyjson
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import dirtyjson

load_dotenv()


class LocalLLMService:
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

    def generate_json(self, prompt, data):
        """
        Sends a prompt and data to the local LLM and returns a parsed JSON response.
        """
        try:
            full_prompt = f"""
                {prompt}

                STRICT RULES:
                1. Return ONLY the valid JSON. No conversational text or markdown code blocks.
                2. Ensure the output is a valid JSON.

                Payload to process:
                {json.dumps(data)}
            """

            response = self.chat_completion(
                # TODO: chamar prompt base como role system
                messages=[{"role": "user", "content": full_prompt}]
            )

            content = response.choices[0].message.content
            clean_text = (
                content.replace("```json", "")
                .replace("```", "")
                .replace("\\", "\\\\")
                .strip()
            )

            # TODO: garantir o json correto
            return dirtyjson.loads(clean_text)
        except json.JSONDecodeError as e:
            print(f"Erro na posição {e.pos}: {e.msg}")
            print("Trecho:", raw_data[max(0, e.pos - 20) : e.pos + 20])
        except Exception as e:
            print(f"Error in generate_json: {e}")
            raise e
