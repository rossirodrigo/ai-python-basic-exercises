from anyio import sleep
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

email_bodies = [
    "Olá, conforme conversamos, seguem em anexo os relatórios de vendas do último trimestre. Fico à disposição para dúvidas.",
    "Oi, tudo bem? Notei que você esqueceu seu casaco aqui em casa ontem. Quer passar aqui para pegar ou prefiro que eu leve?",
    "Prezado cliente, sua fatura com vencimento em 10/05 já está disponível para pagamento. Utilize o código de barras abaixo.",
    "Parabéns! Você foi selecionado para a próxima etapa do nosso processo seletivo. Por favor, escolha um horário na agenda.",
    "Ei, você viu o lançamento daquela série que comentamos? O primeiro episódio saiu hoje e está sensacional!",
    "Confirmamos o recebimento do seu pedido #45892. Ele já está em fase de separação e será enviado em breve.",
    "Bom dia, equipe. Reunião de alinhamento reagendada para as 14h devido a um conflito de salas. Conto com todos.",
    "Você recebeu um novo comentário na sua foto: 'Que lugar incrível! Onde fica esse parque?'. Clique para responder.",
    "Prezados, informamos que a manutenção preventiva da rede elétrica ocorrerá neste domingo, das 08h às 12h.",
    "Olá! Faz tempo que não te vemos por aqui. Use o cupom VOLTOU20 e ganhe 20% de desconto na sua próxima compra.",
    "Segue o link para a votação da nova logo do projeto. Por favor, enviem seus votos até o final do dia de hoje.",
    "Lembrete: Sua consulta com o Dr. Ricardo está agendada para amanhã, às 09h30. Responda 'SIM' para confirmar.",
    "Obrigado por se inscrever em nossa newsletter! A partir de agora, você receberá as melhores dicas de jardinagem.",
    "Atenção: Identificamos um login suspeito na sua conta a partir de um novo dispositivo em Curitiba, Brasil.",
    "Oi, mãe! Só passando para avisar que cheguei bem de viagem. O voo atrasou um pouco, mas correu tudo certo. Beijos!",
    "Solicito a gentileza de revisar o contrato anexo e assinar digitalmente até sexta-feira para evitarmos atrasos.",
    "Temos o prazer de convidar você para o workshop 'Futuro da IA', que acontecerá no auditório principal na próxima semana.",
    "Infelizmente, informamos que o item 'Teclado Mecânico RGB' está fora de estoque. Deseja trocar por um modelo similar?",
    "Caro vizinho, peço desculpas pelo barulho da reforma hoje cedo. Prometo que os trabalhos pesados terminam amanhã.",
    "Urgente: Precisamos validar os dados da planilha de orçamento antes da reunião com a diretoria às 16h. Pode verificar?",
]


def summarize_email_body(email_body):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"""
                Lendo o conteúdo do e-mail {email_body}, retorne o conteúdo de forma 
                resumida. Retorne somente o texto.
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


for i, body in enumerate(email_bodies):
    summarized_email_body = summarize_email_body(body)

    with open(f"content/emails.txt", "a", encoding="utf-8") as file:
        file.write(f"Email {i + 1}:\n")
        file.write(summarized_email_body)
        file.write("\n")
