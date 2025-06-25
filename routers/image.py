from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from pathlib import Path
from utils.ocr import image_to_text
from utils.logger import get_user_logger
from config import settings

router = Router()

TMP_DIR = settings.DATABASE_DIR / "tmp"
TMP_DIR.mkdir(parents=True, exist_ok=True)

@router.message(F.photo | F.document.file_id)
async def handle_image(msg: types.Message, state: FSMContext):
    logger = get_user_logger(msg.chat.id)

    # выбираем наибольшее превью
    file_id = msg.photo[-1].file_id if msg.photo else msg.document.file_id
    file = await msg.bot.get_file(file_id)
    img_path = TMP_DIR / f"{file.file_unique_id}.jpg"
    await msg.bot.download_file(file.file_path, destination=img_path)
    logger.info(f"Image saved → {img_path.name}")

    text = image_to_text(img_path)
    txt_path = img_path.with_suffix('.txt')
    txt_path.write_text(text, encoding='utf-8')
    logger.info(f"OCR done, text saved → {txt_path.name}")

    await msg.answer_document(types.FSInputFile(txt_path), caption="Распознанный текст")