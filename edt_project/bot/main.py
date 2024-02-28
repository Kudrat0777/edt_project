from telegram import Bot
from edt_project import settings


def send_telegram_message(chat_id, message):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=message)