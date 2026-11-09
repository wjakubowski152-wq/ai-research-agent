import json
from schemas import ResearchResult
from report import save_report


def test_save_report_creates_json_file(tmp_path, monkeypatch):
    result = ResearchResult(
        topic="Cybersecurity",
        summary="Protection of computer systems.",
        difficulty="beginner",
        keywords=["security", "encryption"],
        key_findings=["MFA improves account security."],
        confidence=0.95,
        sources=["https://example.com"]
    )

    monkeypatch.chdir(tmp_path)

    save_report(result)

    reports_dir = tmp_path / "reports"
    files = list(reports_dir.glob("*.json"))

    assert len(files) == 1
    assert files[0].exists()
    with open(files[0], "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data["topic"] == "Cybersecurity"
    assert saved_data["confidence"] == 0.95
    assert saved_data["keywords"] == ["security", "encryption"]

def test_save_report_creates_multiple_files(tmp_path, monkeypatch):
    result = ResearchResult(
        topic="Cybersecurity",
        summary="Security research.",
        difficulty="beginner",
        keywords=["security"],
        key_findings=["MFA improves security."],
        confidence=0.95,
        sources=["https://example.com"]
    )

    monkeypatch.chdir(tmp_path)

    save_report(result)
    save_report(result)

    reports_dir = tmp_path / "reports"
    files = list(reports_dir.glob("*.json"))

    assert len(files) == 2