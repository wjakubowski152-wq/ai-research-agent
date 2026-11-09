from ai_research import research_topic
import json
from datetime import datetime
from pathlib import Path
from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIError
)
from conversation import trim_history


def save_report(result):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_{timestamp}.json"

    file_path = reports_dir / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            result.model_dump(),
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"\nReport saved to: {file_path}")


def main():
    conversation_history = []

    print("AI RESEARCH AGENT")
    print("Type 'exit' to quit.")



    while True:
        topic = input("\nEnter research topic: ").strip()

        if topic.lower() == "exit":
            print("Goodbye!")
            break

        if not topic:
            print("Please enter a topic.")
            continue

        try:
            result = research_topic(topic, conversation_history)
            print("\n=== RESEARCH REPORT ===")
            print("Topic:", result.topic)

            print("\n=== SUMMARY ===")
            print(result.summary)

            print("\n=== KEY FINDINGS ===")
            for finding in result.key_findings:
                print(f"- {finding}")

            print("\n=== KEYWORDS ===")
            for keyword in result.keywords:
                print(f"- {keyword}")

            print("\n=== SOURCES ===")
            for source in result.sources:
                print(f"- {source}")

            print("\n=== CONFIDENCE ===")
            print(result.confidence)

            save_report(result)

            conversation_history.append({
                "role": "user",
                "content": topic
            })

            conversation_history.append({
                "role": "assistant",
                "content": result.summary
            })

            conversation_history = trim_history(conversation_history)

        except AuthenticationError:
            print("Error: Invalid API key.")

        except RateLimitError:
            print("Error: API rate limit exceeded.")

        except APIConnectionError:
            print("Error: Could not connect to OpenAI API.")

        except APIError as error:
            print(f"OpenAI API error: {error}")


if __name__ == "__main__":
    main()