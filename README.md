# YojanaAI

An AI assistant for discovering Indian government schemes.

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
```

Set `GEMINI_API_KEY` in `.env` when configuring Gemini integration.

## Run

```bash
uvicorn app.main:app --reload
```

The health endpoint is available at `/api/v1/health`.

## Test

```bash
pytest
```
