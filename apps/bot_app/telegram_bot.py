from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from django.conf import settings
from django.contrib.auth.models import User
from .models import CivilComplaint

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN  # Используйте токен из настроек Django

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Этот бот предназначен для обработки гражданских обращений.')

def process_complaint(update: Update, context: CallbackContext) -> None:
    user, created = User.objects.get_or_create(telegram_user_id=update.message.from_user.id)
    user_complaints = CivilComplaint.objects.filter(user=user, is_resolved=False)

    if user_complaints.exists():
        update.message.reply_text('У вас уже есть открытое обращение. Пожалуйста, дождитесь ответа.')
    else:
        update.message.reply_text('Пожалуйста, опишите свое обращение.')
        context.user_data['complaint_in_progress'] = True

def receive_complaint(update: Update, context: CallbackContext) -> None:
    if 'complaint_in_progress' in context.user_data:
        user, _ = User.objects.get_or_create(telegram_user_id=update.message.from_user.id)
        text = update.message.text
        CivilComplaint.objects.create(user=user, text=text)
        update.message.reply_text('Ваше обращение успешно зарегистрировано. Ожидайте ответа.')
        del context.user_data['complaint_in_progress']
    else:
        update.message.reply_text('Чтобы подать обращение, воспользуйтесь командой /complaint.')

def setup_telegram_dispatcher():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("complaint", process_complaint))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_complaint))

    return updater
