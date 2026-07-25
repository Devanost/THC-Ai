# THC Ai - Advanced Agentic Terminal Assistant

THC Ai is a premium terminal-based AI assistant built in Python. It features an agentic reasoning loop, built-in system tools, a dynamic skill system, and persistent memory.

## Features

- **Premium Terminal UI**: Built with `rich` for markdown rendering, syntax highlighting, and live streaming.
- **Agentic Loop**: Autonomous tool execution (read/write files, run commands, list directories).
- **Skill System**: Dynamically loads instructions from `.thc-skills/` folders.
- **Slash Commands**: `/clear`, `/skills`, `/history`, `/exit`, `/help`.
- **Persistent Memory**: SQLite-backed session history.
- **Local Routing**: Compatible with Ollama and OmniRoute local endpoints.

## Installation

1. Clone the repository or copy the files.
2. Install dependencies:

```bash
pip install rich openai python-dotenv
```

## Configuration

Set environment variables to customize the backend:

```bash
export THC_API_BASE="http://localhost:20128/v1" # or http://localhost:11434/v1 for Ollama
export THC_API_KEY="your-api-key"
export THC_MODEL="gpt-4o"
```

## Usage

Run the assistant:

```bash
python3 -m thc_ai.src.main
```

## Project Structure

- `src/main.py`: Entry point.
- `src/agent.py`: Agentic loop and LLM integration.
- `src/ui.py`: Terminal UI rendering with `rich`.
- `src/tools.py`: Built-in system tools.
- `src/skills.py`: Skill management system.
- `src/memory.py`: SQLite session persistence.
- `src/commands.py`: Slash command handling.
- `src/config.py`: Global configuration.
```
