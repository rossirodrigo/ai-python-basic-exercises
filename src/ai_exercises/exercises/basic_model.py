from ai_exercises.services import GeminiService


def main():
    text = input("Digite o texto: ")

    response = GeminiService().send_message(
        f"Lendo o texto {text}, retorne uma opinião contrária, com argumentos. Retorne apenas o texto, sem explicação.",
    )

    print(response.text)


if __name__ == "__main__":
    main()
