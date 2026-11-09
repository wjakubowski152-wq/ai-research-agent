# AI Research Agent

An AI-powered research assistant built with Python and the OpenAI API.

## Features

- Web search using OpenAI Responses API
- Structured outputs with Pydantic
- Conversation memory
- JSON report export
- API error handling
- Unit tests with pytest
- Unit tests for conversation history management
- Report generation and error handling tests
- Mocked API response tests
- Structured output validation tests



## Tech Stack

- Python
- OpenAI Python SDK
- OpenAI Responses API
- Pydantic
- pytest
- Git

## Project Structure

```text
ai-research-agent/
├── tests/
│   ├── test_conversations.py
│   ├── test_display.py
│   ├── test_mocking.py
│   ├── test_report.py
│   ├── test_schema.py
│   └── test_web_search.py
├── main.py
├── ai_research.py
├── schemas.py
├── conversation.py
├── report.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
## Setup

1. Clone the repository

```bash
git clone https://github.com/wjakubowski152-wq/ai-research-agent.git
cd ai-research-agent
```

2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Configure environment

Create .env in the project root:
```bash
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_supported_model
```

Never publish your API key.
5. Run the application
```bash
python main.py
```

6. Run tests
```bash
pytest -v
```
## Author:
#### Wojciech Jakubowski

