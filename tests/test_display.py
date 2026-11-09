from main import display_report
from schemas import ResearchResult

def test_display_report(capsys):
    result = ResearchResult(
        topic="Python",
        summary="Python is a programming language.",
        difficulty="beginner",
        keywords=["Python", "programming"],
        key_findings=["Python is easy to learn."],
        confidence=0.95,
        sources=["https://example.com"]
    )
    display_report(result)
    captured = capsys.readouterr()
    assert "Python" in captured.out
    assert "Python is a programming language." in captured.out
    assert "Python is easy to learn." in captured.out

    assert "KEYWORDS" in captured.out
    assert "programming" in captured.out

    assert "SOURCES" in captured.out
    assert "https://example.com" in captured.out

    assert "CONFIDENCE" in captured.out
    assert "0.95" in captured.out