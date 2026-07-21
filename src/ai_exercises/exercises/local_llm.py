from ai_exercises.services import LocalLLMService


def main():
    llm = LocalLLMService()

    response = llm.chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"},
        ],
        temperature=1.0,
    )

    print(response)


if __name__ == "__main__":
    main()
