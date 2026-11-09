import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = os.getenv("OPENAI_MODEL")

response = client.responses.create(
    model=model,
    tools=[
        {"type": "web_search"}
    ],
    tool_choice="required",
    input=(
        "Search the web for reliable sources about "
        "cybersecurity risks in hospitals. "
        "Summarize the findings and provide source links."
    )
)

print("\n=== WEB RESEARCH ===")
print(response.output_text)