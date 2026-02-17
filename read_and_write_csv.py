import os
import pandas as pd
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question_list = [
    "Quando será o lançamento da versão 1.0 e o fim do Acesso Antecipado?",
    "Como desbloquear o quarto Aspecto das armas (o Aspecto Oculto)?",
    "Quais são as melhores combinações de Dádivas (builds) para vencer o Chronos?",
    "Onde encontrar e como farmar materiais raros como Bronze e Sedas?",
    "Haverá um sistema de romance tão aprofundado quanto o do primeiro jogo?",
]


def get_answer(question):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"""
                Lendo a pergunta {question}, retorne a resposta de forma muito
                sucinta, em no máximo 100 caracteres, sem separação de linhas
                ou estilos de texto, não inclua vírgula. Retorne somente o texto.
            """,
        )

        return response.text
    except ClientError as e:
        print(f"Client Error: {e.status_code} - {e.response_json.get('message')}")
    except ServerError as e:
        print(f"Server Error: {e.status_code} - {e.response_json.get('message')}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    exit(1)


def write_file(file_path, data, truncate=False):
    with open(file_path, "w" if truncate else "a", encoding="utf-8") as file:
        file.write(data)


for i, question in enumerate(question_list):
    write_file(f"content/questions.txt", question + "\n", truncate=i == 0)

questions_read = []

with open(f"content/questions.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        questions_read.append(line.strip())


write_file(f"content/questions.csv", f"Pergunta,Resposta\n", truncate=True)
for i, question in enumerate(questions_read):
    write_file(f"content/questions.csv", f"{question_list[i]},{get_answer(question)}\n")

df = pd.read_csv("content/questions.csv")

print(df)
