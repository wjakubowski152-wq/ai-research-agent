from pydantic import BaseModel


class ResearchResult(BaseModel):
    topic: str
    summary: str
    difficulty: str
    keywords: list[str]
    key_findings: list[str]
    confidence: float
    sources: list[str]
