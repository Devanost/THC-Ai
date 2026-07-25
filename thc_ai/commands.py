import sys
from thc_ai.config import Config

class CommandHandler:
    def __init__(self, ui, memory, skills_manager):
        self.ui = ui
        self.memory = memory
        self.skills_manager = skills_manager
        self.commands = {
            "/clear": self.clear_context,
            "/skills": self.list_skills,
            "/history": self.view_history,
            "/exit": self.exit_app,
            "/help": self.show_help
        }

    def handle(self, user_input):
        if user_input.startswith("/"):
            cmd = user_input.split()[0]
            if cmd in self.commands:
                self.commands[cmd]()
                return True
            else:
                self.ui.display_error(f"Unknown command: {cmd}")
                return True
        return False

    def clear_context(self):
        self.memory.clear_history()
        self.ui.display_info("Context cleared.")

    def list_skills(self):
        skills = self.skills_manager.get_all_skills()
        if skills:
            self.ui.display_info(f"Active Skills: {', '.join(skills)}")
        else:
            self.ui.display_info("No skills found in .thc-skills/")

    def view_history(self):
        history = self.memory.get_history()
        if not history:
            self.ui.display_info("No history found.")
            return
        
        from rich.table import Table
        table = Table(title="Session History")
        table.add_column("Role", style="cyan")
        table.add_column("Content", style="white")
        
        for msg in history:
            table.add_row(msg["role"], msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"])
        
        self.ui.console.print(table)

    def exit_app(self):
        self.ui.display_info("Goodbye!")
        sys.exit(0)

    def show_help(self):
        help_text = """
Available Commands:
/clear   - Wipe context history
/skills  - List active skills
/history - View past sessions
/exit    - Exit the application
/help    - Show this help message
"""
        self.ui.display_info(help_text)
