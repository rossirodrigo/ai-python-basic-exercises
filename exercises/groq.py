# TODO: https://console.groq.com/keys
# install from pip and connect

from groq import Groq

client = Groq(
    api_key="[ENCRYPTION_KEY]",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain to me how AI works in a few words",
        }
    ],
    model="llama-3.1-8b-instant",
)

print(chat_completion.choices[0].message.content)
