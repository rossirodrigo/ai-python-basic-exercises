import pandas as pd
from services import GeminiService


def main():
    df_reviews = pd.read_csv("content/reviews.csv")

    prompt = """
        Act as a data processor. You will receive a list of dictionaries (JSON-like).
        Your task is to return the EXACT same list, but adding a new key called 'rating' to each object.
        
        Inside 'rating', provide a sentiment analysis strict to three options: Positive, Negative, or Mixed.
        
        RULES:
        1. Keep 'index' and 'text' fields exactly as they are.
    """

    payload = [
        {"index": idx, "text": str(text)}
        for idx, text in df_reviews["reviewText"].items()
    ]

    gemini = GeminiService()
    data = gemini.generate_json(prompt, payload)

    df_reviews["rating"] = None

    for d in data:
        df_reviews.at[d["index"], "rating"] = d["rating"]

    df_reviews.to_csv("content/generated/reviews_with_rating.csv", index=False)

    print("\nProcessing complete! Results saved to 'content/reviews_with_rating.csv'")
    print(df_reviews[["reviewText", "rating"]].head(3))


if __name__ == "__main__":
    main()
