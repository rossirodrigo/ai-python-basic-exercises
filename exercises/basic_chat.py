import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3-flash-preview"
)

while True:
    prompt = input("Send a message (or 'quit' to quit): ")

    if prompt == "quit":
        break
    
    response = chat.send_message(prompt)
    print(response.text)