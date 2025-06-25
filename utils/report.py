from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path
from datetime import datetime
from config import settings
import csv

settings.REPORTS_DIR.mkdir(exist_ok=True)

def _count_users(csv_path: Path) -> int:
    with csv_path.open(newline='', encoding='utf-8') as f:
        return sum(1 for _ in csv.DictReader(f))

def generate_report() -> Path:
    pdf = settings.REPORTS_DIR / f"report_{datetime.utcnow().date()}.pdf"
    c = canvas.Canvas(str(pdf), pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, h-72, "TextRecognizerBot — отчёт")

    c.setFont("Helvetica", 12)
    c.drawString(72, h-110, f"Дата: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    c.drawString(72, h-140, f"Всего пользователей: {_count_users(settings.DATABASE_DIR / 'user.csv')}")

    c.save()
    return pdf