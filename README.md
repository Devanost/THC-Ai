<div align="center">
  <h1>🤖 THC Ai</h1>
  <p><strong>An Advanced, Agentic Terminal AI Assistant</strong></p>
  <p>
    <a href="https://github.com/Devanost/THC-Ai/issues"><img src="https://img.shields.io/github/issues/Devanost/THC-Ai" alt="Issues"></a>
    <a href="https://github.com/Devanost/THC-Ai/network/members"><img src="https://img.shields.io/github/forks/Devanost/THC-Ai" alt="Forks"></a>
    <a href="https://github.com/Devanost/THC-Ai/stargazers"><img src="https://img.shields.io/github/stars/Devanost/THC-Ai" alt="Stars"></a>
    <a href="https://github.com/Devanost/THC-Ai/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Devanost/THC-Ai" alt="License"></a>
  </p>
</div>

---

## 📖 Overview

**THC Ai** is a premium, terminal-based AI assistant built in Python. Designed to mirror the architecture of modern engineering tools like Claude Code, it features an autonomous agentic reasoning loop, built-in system tools, a dynamic skill system, and persistent memory. 

Whether you need to read files, execute shell commands, or manage complex workflows directly from your terminal, THC Ai is built to handle it autonomously.

---

## ✨ Key Features

- 🎨 **Premium Terminal UI**: Built with the `rich` library, featuring live-streaming markdown rendering, syntax-highlighted code blocks, and beautifully colored panels.
- 🧠 **Agentic Loop**: Powered by OpenAI-compatible function calling. The AI can autonomously use built-in tools like `read_file`, `write_file`, `run_command`, and `list_directory`.
- 🛠️ **Dynamic Skill System**: A folder-based architecture (`.thc-skills/`). Drop a `SKILL.md` file into a folder, and the AI dynamically injects its instructions into the context window when relevant.
- ⚡ **Slash Commands**: Quick user controls including `/clear` (wipe context), `/skills` (list active skills), `/history` (view past sessions), and `/exit`.
- 💾 **Persistent Memory**: Retains session history across restarts using a local SQLite database.
- 🔌 **Local LLM Routing**: Easily connect to local endpoints like Ollama or OmniRoute to serve as the local brain.

---

## 🚀 Installation

We provide one-liner installation scripts for all major operating systems.

### Windows (PowerShell)
Open PowerShell as Administrator and run:
```powershell
irm https://raw.githubusercontent.com/Devanost/THC-Ai/main/install.ps1 | iex
```

### Linux / macOS (Bash)
Open your terminal and run:
```bash
curl -sSL https://raw.githubusercontent.com/Devanost/THC-Ai/main/install.sh | bash
```

### Manual Installation
If you prefer to install it manually:
```bash
git clone https://github.com/Devanost/THC-Ai.git
cd THC-Ai
pip install .
```

---

## ⚙️ Configuration

THC Ai is highly customizable via environment variables. By default, it is configured to connect to a local endpoint.

Set the following environment variables in your terminal profile (`.bashrc`, `.zshrc`, or Windows Environment Variables) to customize the backend:

```bash
# Set the API Base URL (e.g., http://localhost:11434/v1 for Ollama)
export THC_API_BASE="http://localhost:20128/v1"

# Set your API Key (if required by your endpoint)
export THC_API_KEY="your-api-key"

# Set the Model Name
export THC_MODEL="gpt-4o"
```

---

## 💻 Usage

Once installed, simply type the following command in your terminal to start the assistant:

```bash
thc-ai
```

### Available Commands inside THC Ai:
- `/help` - Show the help menu.
- `/clear` - Wipe the current context history.
- `/skills` - List all dynamically loaded skills.
- `/history` - View past conversation sessions.
- `/exit` - Close the application.

---

## 📂 Project Structure

```text
THC-Ai/
├── thc_ai/
│   ├── __init__.py
│   ├── main.py         # Application entry point
│   ├── agent.py        # Agentic loop and LLM integration
│   ├── ui.py           # Terminal UI rendering with 'rich'
│   ├── tools.py        # Built-in system tools (read/write/exec)
│   ├── skills.py       # Dynamic skill management system
│   ├── memory.py       # SQLite session persistence
│   ├── commands.py     # Slash command handling
│   └── config.py       # Global configuration
├── .thc-skills/        # Directory for custom skills
├── install.sh          # Linux/macOS installer
├── install.ps1         # Windows installer
├── pyproject.toml      # Package configuration
└── README.md           # This file
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Devanost/THC-Ai/issues).


 ## 🛣️ Future Roadmap

We have exciting plans to expand THC Ai's capabilities:

- **Multi-Model Support**: Integrate with a wider range of LLMs and model providers.
- **Advanced RAG (Retrieval-Augmented Generation)**: Enhance the AI's ability to retrieve and utilize external information more effectively.
- **Plugin System**: Allow users to easily extend THC Ai's functionality with custom plugins and tools.
- **Voice Interface**: Add voice input and output capabilities for a more natural interaction.
- **Cross-Platform Executables**: Provide standalone executables for easier distribution and use without Python installation

---

<div align="center">
  <i>Built with ❤️ for the terminal.</i>
</div>

