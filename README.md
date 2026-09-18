# LLM Providers

An educational Python project for building a small, provider-independent layer
around large language model APIs.

This project was created as part of DEPI training to practice software
engineering fundamentals while working with real LLM tooling. It focuses on
using the OpenAI Python library with Groq's OpenAI-compatible API, managing
configuration, validating structured responses, handling provider errors,
logging requests, and retrying temporary failures.

## What This Project Demonstrates

- Calling Groq through the OpenAI-compatible Python client.
- Keeping provider-specific code behind a gateway interface.
- Generating normal text and structured Pydantic model responses.
- Validating chat messages and ticket classifications with Pydantic.
- Loading secrets and runtime settings from a `.env` file.
- Translating SDK exceptions into application-level exceptions.
- Retrying connection, rate-limit, authentication, and provider failures with
	exponential backoff and jitter.
- Using Python logging to record attempts, delays, and exhausted retries.
- Organizing a Python project with `pyproject.toml` and `uv`.

The example classifies a customer support message into a typed ticket with a
category, sentiment, urgency, and short summary.

## Project Structure

```text
.
|-- pyproject.toml              # Project metadata, dependencies, and command
|-- README.md
`-- src/
		|-- config/
		|   |-- __init__.py
		|   `-- config.py            # Environment-backed application settings
		|-- enums/
		|   |-- llm_error.py         # Standard LLM error messages
		|   `-- roles.py             # System and user message roles
		|-- exceptions/
		|   `-- exceptions.py        # Application-level LLM exceptions
		|-- functions/
		|   `-- generation.py        # Generation helper experiments
		|-- llm_providers/
		|   |-- __init__.py          # Console entry point
		|   |-- main.py              # Structured generation example
		|   `-- test.ipynb           # Notebook experiments
		|-- prompt/
		|   |-- base.py              # Prompt construction helper
		|   `-- summarizer.py        # Support-ticket classification prompt
		|-- providers/
		|   |-- base.py              # Provider interface
		|   |-- gateway.py           # Retry and logging gateway
		|   `-- openai_gateway.py    # OpenAI-compatible provider adapter
		`-- schema/
				|-- __init__.py
				|-- chat.py              # Message and chat request models
				`-- ticket.py            # Structured ticket response model
```

## Requirements

- Python 3.13 or newer
- A [Groq API key](https://console.groq.com/keys)
- [`uv`](https://docs.astral.sh/uv/) for environment and dependency management

## Installation

Clone the repository and enter its directory:

```bash
git clone <repository-url>
cd LLM_providers
```

Create the environment and install the project:

```bash
uv sync
```

The source uses `pydantic-settings` for `.env` loading. If it is not already
installed in your environment, add it to the project with:

```bash
uv add pydantic-settings
```

## Configuration

Create a `.env` file in the project root. Do not commit this file or expose
your API key.

```dotenv
GROQ_API_KEY=your-groq-api-key
BASE_URL=https://api.groq.com/openai/v1
MODEL_NAME=your-supported-groq-model
TIME_OUT=30
MAX_ATTEMPTS=3
BASE_DELAY=1
```

`BASE_URL` defaults to the Groq OpenAI-compatible endpoint, but it can be
changed to another compatible provider. `MAX_ATTEMPTS` and `BASE_DELAY`
control retry behavior in the gateway.

## Running the Project

Run the packaged console entry point:

```bash
uv run llm-providers
```

This currently runs the package scaffold and prints a greeting. To run the
actual structured-generation example in `src/llm_providers/main.py`, use:

```bash
uv run python -m llm_providers.main
```

The example sends a sample laptop-support ticket to the configured model and
prints the structured result. The retry gateway also writes request activity
to `info.log` in the project root.

## Architecture

```text
Application
		|
		v
Gateway (logging, retries, backoff)
		|
		v
LLMbase interface
		|
		v
OpenAIGateway (OpenAI client + Groq endpoint)
		|
		v
Groq API
```

The application passes a `Chat` model to the gateway. `OpenAIGateway` converts
that model into the provider request format. For structured generation, the
provider parses the result into the `Ticket` Pydantic model, so callers can
work with validated data instead of untrusted JSON strings.

## Development Notes

- Keep API keys in environment variables, never in source code.
- Add new providers by implementing the `LLMbase` interface and registering
	the adapter behind the gateway.
- Keep provider SDK exceptions inside the provider adapter and expose the
	project exceptions to the rest of the application.
- Update `pyproject.toml` whenever a new runtime dependency is introduced.
- The notebook under `src/llm_providers/test.ipynb` is available for manual
	experiments.

## Learning Goals

This project is intentionally small so each engineering concern is visible.
It provides practice with API integration, abstraction, configuration,
validation, exception design, logging, retry strategies, environment setup,
and maintainable Python project structure.
