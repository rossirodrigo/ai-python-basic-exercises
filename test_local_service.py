from services import LocalLLMService


def test_json_generation():
    llm = LocalLLMService()

    prompt = "Categorize these fruits by color."
    data = ["apple", "banana", "cherry"]

    print("Testing generate_json...")
    try:
        result = llm.generate_json(prompt, data)
        print("Success! Result:")
        print(result)
    except Exception as e:
        print(f"Failed: {e}")


if __name__ == "__main__":
    test_json_generation()
