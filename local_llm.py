from openai import OpenAI


def main():
    client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")

    response = client.chat.completions.create(
        model="google/gemma-3n-e4b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"},
        ],
        temperature=1.0,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
