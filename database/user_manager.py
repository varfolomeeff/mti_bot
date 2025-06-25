import csv
from pathlib import Path
from datetime import datetime

class UserManager:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("chat_id,username,first_seen,last_seen\n", encoding="utf-8")

    def add_or_update(self, chat_id: int, username: str | None):
        rows, found = [], False
        if self.path.exists():
            with self.path.open(newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    if int(row["chat_id"]) == chat_id:
                        row["last_seen"] = datetime.utcnow().isoformat()
                        if username:
                            row["username"] = username
                        found = True
                    rows.append(row)
        if not found:
            rows.append({
                "chat_id": chat_id,
                "username": username or "",
                "first_seen": datetime.utcnow().isoformat(),
                "last_seen": datetime.utcnow().isoformat(),
            })
        with self.path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["chat_id","username","first_seen","last_seen"])
            writer.writeheader()
            writer.writerows(rows)
