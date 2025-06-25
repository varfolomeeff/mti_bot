from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(msg: types.Message):
    await msg.answer(
        "<b>Команды бота</b>\n"
        "/start — начать работу\n"
        "/help — это сообщение\n"
        "/about — о боте\n\n"
        "Отправьте изображение, чтобы получить результат OCR в виде .txt файла."
    )