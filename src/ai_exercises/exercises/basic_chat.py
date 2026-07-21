from ai_exercises.services import GeminiService


def main():
    gemini = GeminiService()
    chat = gemini.create_chat()

    while True:
        prompt = input("Send a message (or 'quit' to quit): ")

        if prompt == "quit":
            break

        response = gemini.send_message(prompt, chat)
        print(response.text)


if __name__ == "__main__":
    main()
