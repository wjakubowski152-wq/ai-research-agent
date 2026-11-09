import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL")

    response = client.responses.create(
        model=model,
        tools=[{"type": "web_search"}],
        tool_choice="required",
        input="Research the latest trends in AI agents in 2026. Provide key findings and sources."
    )

    print(response.output_text)


if __name__ == "__main__":
    main()