# try-adk

A sample project demonstrating the use of [Google Agent Development Kit (ADK)](https://github.com/google/adk-python).

## Features

- Search agent using TavilySearch.
- Time agent providing current time for any timezone.

## Requirements

- Python 3.13+
- uv
- gpt-4o-mini (via Azure OpenAI)

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate    # On Windows
   uv sync
   ```
3. Copy `example.env` to `.env` and fill in your API keys as needed.

## Usage

Run the main entry point:

```bash
adk web
```
