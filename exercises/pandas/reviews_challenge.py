import pandas as pd
import os
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def categorize_reviews(data):
    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=f"""
                Act as a data processor. You will receive a list of dictionaries (JSON-like).
                Your task is to return the EXACT same list, but adding a new key called 'rating' to each object.
                
                Inside 'rating', provide a sentiment analysis strict to three options: Positive, Negative, or Mixed.
                
                STRICT RULES:
                1. Return ONLY the valid JSON list. No conversational text or markdown code blocks.
                2. Keep 'index' and 'text' fields exactly as they are.
                3. Ensure the output is a valid JSON array of objects.

                Payload to process:
                {json.dumps(data)}
            """,
        )

        return json.loads(
            response.text.replace("```json", "").replace("```", "").strip()
        )
    except ClientError as e:
        print(f"Client Error: {e.status_code} - {e.response_json.get('message')}")
    except ServerError as e:
        print(f"Server Error: {e.status_code} - {e.response_json.get('message')}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    exit(1)


df_reviews = pd.read_csv("content/reviews.csv")

payload = [
    {"index": idx, "text": str(text)} for idx, text in df_reviews["reviewText"].items()
]

data = categorize_reviews(payload)

df_reviews["rating"] = None

for d in data:
    df_reviews.at[d["index"], "rating"] = d["rating"]

df_reviews.to_csv("content/reviews_with_rating.csv", index=False)
