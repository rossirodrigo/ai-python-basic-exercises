import pandas as pd

from ai_exercises.paths import GENERATED_DATA_DIR, RAW_DATA_DIR
from ai_exercises.services import GeminiService

PROMPT = """
    Act as a data processor. You will receive a list of dictionaries (JSON-like).
    Your task is to return the EXACT same list, but adding a new key called 'rating' to each object.

    Inside 'rating', provide a sentiment analysis strict to three options: Positive, Negative, or Mixed.

    RULES:
    1. Keep 'index' and 'text' fields exactly as they are.
"""


def main():
    df_reviews = pd.read_csv(RAW_DATA_DIR / "reviews.csv")

    payload = [
        {"index": idx, "text": str(text)}
        for idx, text in df_reviews["reviewText"].items()
    ]

    gemini = GeminiService()
    data = gemini.generate_json(PROMPT, payload)

    df_reviews["rating"] = None

    for d in data:
        df_reviews.at[d["index"], "rating"] = d["rating"]

    output_path = GENERATED_DATA_DIR / "reviews_with_rating.csv"
    df_reviews.to_csv(output_path, index=False)

    print(f"\nProcessing complete! Results saved to '{output_path}'")
    print(df_reviews[["reviewText", "rating"]].head(3))


if __name__ == "__main__":
    main()
