import pandas as pd

from ai_exercises.paths import GENERATED_DATA_DIR, RAW_DATA_DIR
from ai_exercises.services import GeminiService, GroqService, LocalLLMService

SERVICES = {
    "gemini": GeminiService,
    "groq": GroqService,
    "local": LocalLLMService,
}

PROMPT = """
    Act as a data processor. You will receive a list of dictionaries (JSON-like).
    Your task is to return the EXACT same list, but adding two new keys called 'translation' and 'rating' to each object.

    Inside 'translation', provide a translation of the 'review' field to English.

    Inside 'rating', provide a sentiment analysis strict to three options: Positive, Negative, or Mixed.

    RULES:
    1. Keep 'id', 'user' and 'review' fields exactly as they are.
"""


def process_file_lines(file_path):
    reviews = []

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            reviews.append(line.strip())

    return reviews


def parse_reviews(raw_lines):
    reviews_split = []

    for review in raw_lines:
        split = review.split("$")
        reviews_split.append(
            {
                "id": split[0] or None,
                "user": split[1] or None,
                "review": split[2] or None,
            }
        )

    return reviews_split


def build_result_dataframe(result):
    return (
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


def main(llm_name: str):
    reviews = process_file_lines(RAW_DATA_DIR / "reviews.txt")
    reviews_split = parse_reviews(reviews)

    llm = SERVICES[llm_name]()
    result = llm.generate_json(PROMPT, reviews_split)

    df_reviews = build_result_dataframe(result)

    df_reviews.to_csv(GENERATED_DATA_DIR / "reviews_challenge_processed.csv", index=True)

    print(df_reviews.head(5))


def cli():
    llm_name = input(f"Choose LLM ({', '.join(SERVICES)}): ")

    if llm_name not in SERVICES:
        raise ValueError("Invalid LLM")

    main(llm_name)


if __name__ == "__main__":
    cli()
