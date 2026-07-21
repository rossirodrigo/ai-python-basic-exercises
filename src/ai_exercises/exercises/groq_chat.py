from ai_exercises.services import GroqService


def main():
    groq = GroqService()

    response = groq.chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful and concise assistant."},
            {
                "role": "user",
                "content": "What time is it in Brazil right now?",
            },
        ],
        temperature=0.5,
    )

    print(response)


if __name__ == "__main__":
    main()
