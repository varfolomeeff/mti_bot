from decouple import config
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

class Settings:
    BOT_TOKEN: str = config("BOT_TOKEN")
    TESSERACT_CMD: str = config("TESSERACT_CMD", default="/usr/bin/tesseract")
    ADMIN_IDS: list[int] = [int(x) for x in config("ADMIN_IDS", default="").split(',') if x]

    LOG_DIR = BASE_DIR / "logs"
    DATABASE_DIR = BASE_DIR / "database"
    REPORTS_DIR = BASE_DIR / "reports"
    ABOUT_FILE = BASE_DIR / "about.json"

    @property
    def about(self) -> dict:
        return json.loads(self.ABOUT_FILE.read_text(encoding="utf-8"))

settings = Settings()
