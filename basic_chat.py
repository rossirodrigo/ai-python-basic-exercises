from services.gemini_service import GeminiService

gemini = GeminiService()
chat = gemini.create_chat()

while True:
    prompt = input("Send a message (or 'quit' to quit): ")

    if prompt == "quit":
        break

    response = gemini.send_message(prompt, chat)
    print(response.text)
