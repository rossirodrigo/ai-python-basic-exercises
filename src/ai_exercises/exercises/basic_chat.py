from ai_exercises.services import GeminiService


def main():
    gemini = GeminiService()
    messages = []

    while True:
        prompt = input("Send a message (or 'quit' to quit): ")

        if prompt == "quit":
            break

        messages.append({"role": "user", "content": prompt})
        reply = gemini.chat_completion(messages)
        messages.append({"role": "assistant", "content": reply})
        print(reply)


if __name__ == "__main__":
    main()
