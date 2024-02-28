# yourappname/telegram_bot.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from django.conf import settings
from .models import CivilComplaint
from .forms import EmployeeResponseForm
from edt_project import settings

TELEGRAM_TOKEN = settings.TELEGRAM_BOT_TOKEN  # Замените на ваш токен

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Этот бот предназначен для обработки гражданских обращений.')

def process_complaint(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_complaints = CivilComplaint.objects.filter(user__telegram_user_id=user_id, is_resolved=False)

    if user_complaints.exists():
        update.message.reply_text('У вас уже есть открытое обращение. Пожалуйста, дождитесь ответа.')
    else:
        update.message.reply_text('Пожалуйста, опишите свое обращение.')
        context.user_data['complaint_in_progress'] = True

def receive_complaint(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id

    if 'complaint_in_progress' in context.user_data:
        text = update.message.text
        CivilComplaint.objects.create(user_id=user_id, text=text)
        update.message.reply_text('Ваше обращение успешно зарегистрировано. Ожидайте ответа.')
        del context.user_data['complaint_in_progress']
    else:
        update.message.reply_text('Чтобы подать обращение, воспользуйтесь командой /complaint.')

def notify_unresolved_complaints(context: CallbackContext) -> None:
    unresolved_complaints = CivilComplaint.objects.filter(is_resolved=False)
    
    if unresolved_complaints.exists():
        for complaint in unresolved_complaints:
            message = f"Новое обращение от пользователя {complaint.user.username}: {complaint.text}"
            context.bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)

def setup_telegram_dispatcher() -> None:
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("complaint", process_complaint))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_complaint))

    return updater
