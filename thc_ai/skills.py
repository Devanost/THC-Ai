import os
from thc_ai.config import Config

class SkillsManager:
    def __init__(self, skills_dir=Config.SKILLS_DIR):
        self.skills_dir = skills_dir
        self.skills = {}
        self.load_skills()

    def load_skills(self):
        if not os.path.exists(self.skills_dir):
            os.makedirs(self.skills_dir)
            return

        for skill_folder in os.listdir(self.skills_dir):
            skill_path = os.path.join(self.skills_dir, skill_folder)
            if os.path.isdir(skill_path):
                skill_md = os.path.join(skill_path, "SKILL.md")
                if os.path.exists(skill_md):
                    with open(skill_md, 'r') as f:
                        self.skills[skill_folder] = f.read()

    def get_all_skills(self):
        return list(self.skills.keys())

    def get_relevant_skills(self, user_input):
        # Simple keyword matching for demo, can be improved with embeddings
        relevant = []
        for name, content in self.skills.items():
            if name.lower() in user_input.lower():
                relevant.append(f"Skill: {name}\nInstructions: {content}")
        return relevant
