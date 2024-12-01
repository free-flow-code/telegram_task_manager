import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties

from config import settings
from logger_init import logger
from handlers.register_user import router as user_router


async def main():
    logger.info("Starting Bot")

    bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(user_router)

    dp.startup.register(set_main_menu)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def set_main_menu(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="/start", description="Начать работу"),
            types.BotCommand(command="/add", description="Добавить задачу"),
            types.BotCommand(command="/tasks", description="Просмотреть задачи"),
            types.BotCommand(command="/manage", description="Управление задачами"),
            types.BotCommand(command="/search", description="Поиск задач"),
        ]
    )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")
