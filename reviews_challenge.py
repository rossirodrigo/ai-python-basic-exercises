from services.gemini_service import GeminiService
from services import LocalLLMService
import pandas as pd


def process_file_lines(file_path: str):
    reviews = []

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            reviews.append(line.strip())

    return reviews


def main(local: bool):
    reviews = process_file_lines("content/reviews.txt")
    reviews_split = []

    for review in reviews:
        split = review.split("$")
        reviews_split.append(
            {
                "id": split[0] or None,
                "user": split[1] or None,
                "review": split[2] or None,
            }
        )

    prompt = """
        Act as a data processor. You will receive a list of dictionaries (JSON-like).
        Your task is to return the EXACT same list, but adding two new keys called 'translation' and 'rating' to each object.
        
        Inside 'translation', provide a translation of the 'review' field to English.
        
        Inside 'rating', provide a sentiment analysis strict to three options: Positive, Negative, or Mixed.
        
        RULES:
        1. Keep 'id', 'user' and 'review' fields exactly as they are.
    """

    llm = LocalLLMService() if local else GeminiService()
    result = llm.generate_json(prompt, reviews_split)

    df_reviews = (
        pd.DataFrame(
            {
                "id": [review["id"] for review in result],
                "user": [review["user"] for review in result],
                "review": [review["review"] for review in result],
                "translation": [review["translation"] for review in result],
                "rating": [review["rating"] for review in result],
            }
        )
        .set_index("id")
        .sort_values(
            by="rating", key=lambda x: x.map({"Positive": 1, "Negative": 2, "Mixed": 3})
        )
    )

    df_reviews.to_csv("content/generated/reviews_challenge_processed.csv", index=True)

    print(df_reviews.head(5))


if __name__ == "__main__":
    llm = input("Choose LLM (gemini, local): ")

    if llm not in ["gemini", "local"]:
        raise ValueError("Invalid LLM")

    main(llm == "local")
