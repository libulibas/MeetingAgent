# MeetingAgent

Turns raw meeting notes into a summary, action items, and a follow-up email.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env  # add your ANTHROPIC_API_KEY
```

## Usage

```bash
cat notes.txt | python meeting_agent.py
```

## Model

`claude-sonnet-4-20250514` via the Anthropic Python SDK.

## License

MIT
