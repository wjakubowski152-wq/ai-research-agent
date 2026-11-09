import pytest
from pydantic import ValidationError
from schemas import ResearchResult


def test_research_result_valid_data():
    result = ResearchResult(
        topic="Cybersecurity",
        summary="Protection of computer systems and networks.",
        difficulty="beginner",
        key_findings=[
            "Hospitals are vulnerable to ransomware.",
            "MFA helps protect user accounts."
        ],
        keywords=[
            "network security",
            "encryption",
            "authentication",
        ],
        confidence=0.97,
        sources=["https://example.com"]
    )

    assert result.topic == "Cybersecurity"
    assert result.confidence == 0.97
    assert len(result.keywords) == 3

def test_research_result_missing_required_field():
    with pytest.raises(ValidationError):
        ResearchResult(
            topic="Cybersecurity",
            summary="Protection of computer systems.",
            difficulty="beginner",
            keywords=["security"],
            confidence=0.97,
            sources=["https://example.com"]
        )