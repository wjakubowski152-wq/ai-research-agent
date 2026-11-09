import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured")

    if not model:
        raise ValueError("OPENAI_MODEL is not configured")

    return api_key, model


OPENAI_API_KEY, OPENAI_MODEL = load_config()