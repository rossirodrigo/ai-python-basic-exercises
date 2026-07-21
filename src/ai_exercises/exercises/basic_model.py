from ai_exercises.services import GeminiService


def main():
    text = input("Digite o texto: ")

    response = GeminiService().chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"Lendo o texto {text}, retorne uma opinião contrária, com argumentos. Retorne apenas o texto, sem explicação.",
            }
        ],
    )

    print(response)


if __name__ == "__main__":
    main()
