from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from config import settings
from database.user_manager import UserManager
from utils.logger import get_user_logger
from keyboards.reply import main_menu
from routers.help import cmd_help
from routers.about import cmd_about
from aiogram import F

router = Router()
user_db = UserManager(settings.DATABASE_DIR / "user.csv")

@router.message(CommandStart())
async def cmd_start(msg: types.Message, state: FSMContext):
    user_db.add_or_update(msg.chat.id, msg.from_user.username)
    get_user_logger(msg.chat.id).info("/start")
    await msg.answer(
        f"Привет, {msg.from_user.full_name}! «TextRecognizerBot» готов к работе.\n"
        "Просто отправь картинку — верну .txt с текстом.",
        reply_markup=main_menu(),
    )

@router.message(F.text == "📄 Помощь (/help)")
async def main_menu_help(msg: types.Message, state: FSMContext):
    await cmd_help(msg)

@router.message(F.text == "ℹ️ О боте (/about)")
async def main_menu_about(msg: types.Message, state: FSMContext):
    await cmd_about(msg)