from services.gemini_service import GeminiService

text = input("Digite o texto: ")

response = GeminiService().send_message(
    f"Lendo o texto {text}, retorne uma opinião contrária, com argumentos. Retorne apenas o texto, sem explicação.",
)

print(response.text)
