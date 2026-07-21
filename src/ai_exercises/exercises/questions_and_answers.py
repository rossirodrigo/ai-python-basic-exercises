import pandas as pd

from ai_exercises.paths import GENERATED_DATA_DIR, RAW_DATA_DIR
from ai_exercises.services import GeminiService

PROMPT = """
    Act as a data processor. You will receive a list in an array format.
    Your task is to a JSON format, adding the original text in a key called 'question' and an answer in a key called 'answer'.

    All questions are related to the game Hades II.

    STRICT RULES:
    1. The answer should be in Portuguese.
    2. The answer should be concise and straight to the point.
    3. The answer should be in a maximum of 100 characters.
    4. The answer should not contain any special characters.
    5. The answer should not contain any emojis.
    6. The answer should not contain any markdown code blocks.
    7. The answer should not contain any conversational text.
    8. The answer should not contain any special characters.
    9. The answer should not contain any emojis.
    10. The answer should not contain any markdown code blocks.
    11. The answer should not contain any conversational text.
"""


def main():
    questions = []

    with open(RAW_DATA_DIR / "questions.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            questions.append(line.strip())

    llm = GeminiService()
    result = llm.generate_json(PROMPT, questions)

    df_questions = pd.DataFrame(
        {
            "question": [question["question"] for question in result],
            "answer": [question["answer"] for question in result],
        }
    ).set_index("question")

    df_questions.to_csv(GENERATED_DATA_DIR / "answers.csv")

    print(df_questions)


if __name__ == "__main__":
    main()
