from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .telegram_bot import notify_unresolved_complaints

@shared_task
def notify_unresolved_complaints_task():
    notify_unresolved_complaints()

def setup_periodic_task():
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=10,  # Периодичность в секундах
        period=IntervalSchedule.SECONDS,
    )
    PeriodicTask.objects.get_or_create(
        interval=schedule,
        name='Notify unresolved complaints',
        task='yourappname.tasks.notify_unresolved_complaints_task',  # Убедитесь, что здесь правильно указан путь
        enabled=True,
        one_off=False,  # Задача будет выполняться регулярно, а не однократно
    )
