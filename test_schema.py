from schemas import ResearchResult


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
    sources=["https://www.microsoft.com/pl-pl/security/business/security-101/what-is-cybersecurity", "https://cybersecurity.pl/", "https://codeme.pl/czym-jest-cybersecurity-i-dlaczego-powinno-nas-interesowac/"]
)
print(result.topic)
print(result.difficulty)
print(result.keywords)

print("\nJSON output:")
print(result.model_dump_json(indent=4))
