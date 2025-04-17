# try-adk

A sample project demonstrating the use of (Google ADK agents)[https://github.com/google/adk-python].

## Features

- Search agent using TavilySearch.
- Time agent providing current time for any timezone.

## Requirements

- Python 3.13+
- uv

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Copy `example.env` to `.env` and fill in your API keys as needed.

## Usage

Run the main entry point:

```bash
adk run search_agent

# or

adk run test_agent
```
