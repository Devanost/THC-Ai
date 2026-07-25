import sys
from thc_ai.ui import UIRenderer
from thc_ai.memory import Memory
from thc_ai.skills import SkillsManager
from thc_ai.agent import Agent
from thc_ai.commands import CommandHandler
from thc_ai.config import Config

def main():
    ui = UIRenderer()
    memory = Memory()
    skills_manager = SkillsManager()
    agent = Agent(ui, memory, skills_manager)
    cmd_handler = CommandHandler(ui, memory, skills_manager)

    ui.display_welcome()

    while True:
        try:
            user_input = ui.console.input(f"\n[bold {Config.THEME_COLOR}]THC Ai[/bold {Config.THEME_COLOR}] > ").strip()
            
            if not user_input:
                continue

            if cmd_handler.handle(user_input):
                continue

            agent.run(user_input)

        except KeyboardInterrupt:
            ui.display_info("\nUse /exit to quit.")
        except Exception as e:
            ui.display_error(str(e))

if __name__ == "__main__":
    main()
