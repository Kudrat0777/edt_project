from django.core.management.base import BaseCommand
from apps.bot_app.telegram_bot import setup_telegram_dispatcher

class Command(BaseCommand):
    help = 'Starts the telegram bot.'

    def handle(self, *args, **options):
        updater = setup_telegram_dispatcher()
        updater.start_polling()
        updater.idle()  # Ждет до прерывания командой Ctrl+C
