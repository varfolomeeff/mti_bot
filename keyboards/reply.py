from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="📄 Помощь (/help)")
    kb.button(text="ℹ️ О боте (/about)")
    return kb.as_markup(resize_keyboard=True)