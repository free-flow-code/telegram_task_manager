import os
import logging
from logging.handlers import RotatingFileHandler

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("TASKY_bot")
logger.setLevel(logging.DEBUG)

bot_handler = RotatingFileHandler(
    os.path.join(log_dir, "tasky-bot.log"),
    mode="w",
    maxBytes=5 * 1024 * 1024,  # Максимальный размер файла 5 МБ
    backupCount=3,  # Хранить до 3 резервных файлов
    encoding="utf-8"
)
bot_handler.setLevel(logging.DEBUG)
app_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
bot_handler.setFormatter(app_formatter)
logger.addHandler(bot_handler)
