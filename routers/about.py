from aiogram import Router, types
from aiogram.filters import Command
from config import settings

router = Router()

@router.message(Command("about"))
async def cmd_about(msg: types.Message):
    about = settings.about
    text = (
        f"<b>{about['bot_name']}</b>\n\n"
        f"{about['description']}\n\n"
        f"Автор(ы): {', '.join(about['authors'])}\n"
        f"Функциональность: {about['functionality']}\n\n"
        f"<b>Команды</b>:\n" +
        "\n".join(f"{c['command']} — {c['description']}" for c in about['commands'])
    )
    await msg.answer(text)