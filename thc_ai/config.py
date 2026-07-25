import os

class Config:
    PROJECT_NAME = "THC Ai"
    VERSION = "1.0.0"
    
    # API Configuration
    # Default to OmniRoute or Ollama as requested
    API_BASE_URL = os.getenv("THC_API_BASE", "http://localhost:20128/v1")
    API_KEY = os.getenv("THC_API_KEY", "not-needed")
    MODEL = os.getenv("THC_MODEL", "gpt-4o") # Or your local model name
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SKILLS_DIR = os.path.join(os.getcwd(), ".thc-skills")
    DB_PATH = os.path.join(os.getcwd(), "thc_history.db")
    
    # UI Settings
    THEME_COLOR = "cyan"
    USER_COLOR = "green"
    AI_COLOR = "bright_white"
    TOOL_COLOR = "yellow"
