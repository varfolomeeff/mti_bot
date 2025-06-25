import logging
from pathlib import Path
from config import settings

settings.LOG_DIR.mkdir(exist_ok=True)

_DEF_FMT = logging.Formatter("%(asctime)s — %(message)s")

def get_user_logger(chat_id: int):
    logger = logging.getLogger(str(chat_id))
    if not logger.handlers:
        fh = logging.FileHandler(settings.LOG_DIR / f"{chat_id}.log", encoding="utf-8")
        fh.setFormatter(_DEF_FMT)
        logger.setLevel(logging.INFO)
        logger.addHandler(fh)
    return logger
