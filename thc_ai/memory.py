import sqlite3
import json
from datetime import datetime
from thc_ai.config import Config

class Memory:
    def __init__(self, db_path=Config.DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    role TEXT,
                    content TEXT
                )
            """)

    def save_message(self, role, content):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO sessions (timestamp, role, content) VALUES (?, ?, ?)",
                (datetime.now().isoformat(), role, content)
            )

    def get_history(self, limit=50):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT role, content FROM sessions ORDER BY id ASC LIMIT ?",
                (limit,)
            )
            history = cursor.fetchall()
            return [{"role": role, "content": content} for role, content in history]

    def clear_history(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM sessions")
