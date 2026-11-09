from unittest.mock import MagicMock
from unittest.mock import patch
from schemas import ResearchResult
from ai_research import research_topic
import pytest
from openai import RateLimitError, APIConnectionError
import httpx


def test_mock_api_response():
    mock_api = MagicMock()

    mock_api.output_text = "This is a test response."

    assert mock_api.output_text == "This is a test response."

def test_mock_function():
    with patch("builtins.print") as mock_print:
        print("Hello AI")

        mock_print.assert_called_once_with("Hello AI")

def test_mock_function_call():
    mock_api = MagicMock()

    mock_api.generate.return_value = "AI response"

    result = mock_api.generate("Research Python")

    assert result == "AI response"
    mock_api.generate.assert_called_once_with("Research Python")

def test_research_topic_returns_structured_result():
    mock_result = ResearchResult(
        topic="Python",
        summary="Python is a programming language.",
        difficulty="beginner",
        keywords=["Python", "programming"],
        key_findings=["Python is widely used in AI."],
        confidence=0.95,
        sources=["https://example.com"]
    )

    with patch("ai_research.client.responses.parse") as mock_parse:
        mock_parse.return_value.output_parsed = mock_result

        result = research_topic("Python", [])

        assert result.topic == "Python"
        assert result.summary == "Python is a programming language."

        mock_parse.assert_called_once()
        call_args = mock_parse.call_args

        assert call_args.kwargs["model"] is not None
        assert call_args.kwargs["tool_choice"] == "required"
        assert call_args.kwargs["text_format"] == ResearchResult
        input_messages = call_args.kwargs["input"]

        assert input_messages[0]["role"] == "system"
        assert input_messages[1]["content"] == "Research this topic: Python"

def test_research_topic_includes_conversation_history():
    history = [
        {"role": "user", "content": "What is Python?"},
        {"role": "assistant", "content": "Python is a programming language."}
    ]

    mock_result = ResearchResult(
        topic="Python libraries",
        summary="Libraries extend Python functionality.",
        difficulty="beginner",
        keywords=["Python", "libraries"],
        key_findings=["Libraries provide reusable functionality."],
        confidence=0.95,
        sources=["https://example.com"]
    )

    with patch("ai_research.client.responses.parse") as mock_parse:
        mock_parse.return_value.output_parsed = mock_result

        result = research_topic("Python libraries", history)

        input_messages = mock_parse.call_args.kwargs["input"]

        assert input_messages[1] == history[0]
        assert input_messages[2] == history[1]
        assert input_messages[3]["content"] == "Research this topic: Python libraries"
        assert result.topic == "Python libraries"


def test_research_topic_limits_conversation_history():
    history = [
        {"role": "user", "content": f"Message {i}"}
        for i in range(12)
    ]

    mock_result = ResearchResult(
        topic="Python",
        summary="Python research.",
        difficulty="beginner",
        keywords=["Python"],
        key_findings=["Python is popular."],
        confidence=0.95,
        sources=["https://example.com"]
    )

    with patch("ai_research.client.responses.parse") as mock_parse:
        mock_parse.return_value.output_parsed = mock_result

        research_topic("Python", history)

        input_messages = mock_parse.call_args.kwargs["input"]

        assert len(input_messages) == 12
        assert input_messages[0]["role"] == "system"
        assert input_messages[1]["content"] == "Message 2"
        assert input_messages[10]["content"] == "Message 11"
        assert input_messages[11]["content"] == "Research this topic: Python"

def test_research_topic_handles_api_error():
    with patch("ai_research.client.responses.parse") as mock_parse:
        mock_parse.side_effect = ValueError("API error")

        with pytest.raises(ValueError, match="API error"):
            research_topic("Python", [])

def test_research_topic_handles_connection_error():
    with patch("ai_research.client.responses.parse") as mock_parse:
        mock_parse.side_effect = APIConnectionError(request=None)

        with pytest.raises(APIConnectionError):
            research_topic("Python", [])

def test_research_topic_handles_rate_limit_error():
    with patch("ai_research.client.responses.parse") as mock_parse:
        request = httpx.Request("POST", "https://api.openai.com/v1/responses")
        response = httpx.Response(429, request=request)

        mock_parse.side_effect = RateLimitError(
            "Rate limit exceeded",
            response=response,
            body=None
        )

        with pytest.raises(RateLimitError):
            research_topic("Python", [])