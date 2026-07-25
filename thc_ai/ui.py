from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.live import Live
from rich.syntax import Syntax
from rich.table import Table
from rich.theme import Theme
from thc_ai.config import Config

class UIRenderer:
    def __init__(self):
        self.console = Console(theme=Theme({
            "info": "dim cyan",
            "warning": "magenta",
            "danger": "bold red",
            "user": Config.USER_COLOR,
            "ai": Config.AI_COLOR,
            "tool": Config.TOOL_COLOR
        }))

    def display_welcome(self):
        welcome_text = f"# {Config.PROJECT_NAME} v{Config.VERSION}\nAdvanced Agentic Terminal Assistant"
        self.console.print(Panel(Markdown(welcome_text), border_style=Config.THEME_COLOR))

    def print_user_input(self, text):
        self.console.print(f"\n[bold user]>>>[/bold user] {text}")

    def display_tool_call(self, tool_name, args):
        self.console.print(Panel(
            f"Executing: [bold]{tool_name}[/bold]\nArgs: {args}",
            title="Tool Execution",
            border_style=Config.TOOL_COLOR
        ))

    def display_tool_output(self, output):
        self.console.print(Panel(
            str(output),
            title="Tool Output",
            border_style="dim yellow"
        ))

    def stream_ai_response(self, text_iterator):
        full_response = ""
        with Live("", console=self.console, refresh_per_second=10, vertical_overflow="visible") as live:
            for chunk in text_iterator:
                if chunk:
                    full_response += chunk
                    live.update(Panel(Markdown(full_response), title="THC Ai", border_style=Config.THEME_COLOR))
        return full_response

    def display_error(self, error):
        self.console.print(f"[bold danger]Error:[/bold danger] {error}")

    def display_info(self, info):
        self.console.print(f"[info]{info}[/info]")
