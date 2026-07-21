import os

from dotenv import load_dotenv
from groq import Groq


def main():
    load_dotenv()

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful and concise assistant."},
            {
                "role": "user",
                "content": "What time is it in Brazil right now?",
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_tokens=1024,
    )

    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    main()
