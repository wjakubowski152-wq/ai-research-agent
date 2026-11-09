from ai_research import research_topic
from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIError
)
from conversation import trim_history
from report import save_report
from logger_config import logger

def display_report(result):
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


def main():
    conversation_history = []
    logger.info("AI Research Agent started")

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
            display_report(result)

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
            logger.error("Invalid API key.")

        except RateLimitError:
            logger.warning("API rate limit exceeded.")

        except APIConnectionError:
            logger.error("Could not connect to OpenAI API.")

        except APIError as error:
            logger.error(f"OpenAI API error: {error}")
        except Exception:
            logger.exception("Unexpected error during research")


if __name__ == "__main__":
    main()