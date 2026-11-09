
from config import OPENAI_API_KEY, OPENAI_MODEL
from openai import OpenAI
from schemas import ResearchResult
from logger_config import logger

client = OpenAI(api_key=OPENAI_API_KEY)
model = OPENAI_MODEL

def research_topic(
    topic: str,
    conversation_history: list
) -> ResearchResult:
    logger.info(f"Starting research for topic: {topic}")

    input_messages = conversation_history[-10:] + [
        {
            "role": "user",
            "content": f"Research this topic: {topic}"
        }
    ]

    response = client.responses.parse(
        model=model,
        tools=[
            {"type": "web_search"}
        ],
        tool_choice="required",
        input=[
            {
                "role": "system",
                "content": (
                    "You are an AI research assistant. "
                    "Maintain the context of the conversation. "
                    "Use web search to verify current information. "
                    "Do not invent facts or source URLs. "
                    "Return a structured research report."
                )
            },
            *input_messages
        ],
        text_format=ResearchResult
    )

    return response.output_parsed


def main():

    topic = input("Enter research topic: ")

    result = research_topic(topic, [])

    print("\n=== RESEARCH RESULT ===")
    print("Topic:", result.topic)
    print("Summary:", result.summary)
    print("Difficulty:", result.difficulty)
    print("Keywords:", result.keywords)
    print("Confidence:", result.confidence)
    print("Sources:", result.sources)

    print("\n=== JSON ===")
    print(result.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
