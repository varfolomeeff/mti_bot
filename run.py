import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from config import settings
from routers import start, help as help_router, about, image
from utils.report import generate_report
from datetime import datetime, timedelta


async def daily_report_scheduler(bot: Bot):
    while True:
        now = datetime.utcnow()
        next_run = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        await asyncio.sleep((next_run - now).total_seconds())
        pdf_path = generate_report()
        for admin in settings.ADMIN_IDS:
            await bot.send_document(admin, pdf_path.open("rb"), caption="Ежедневный отчёт бота")


async def on_startup(bot: Bot, **_):
    asyncio.create_task(daily_report_scheduler(bot))


async def main():
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(start.router, help_router.router, about.router, image.router)
    dp.startup.register(on_startup)          

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


