import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

text = input("Digite o texto: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Lendo o texto {text}, retorne uma opinião contrária, com argumentos. Retorne apenas o texto, sem explicação.",
)

print(response.text)