from django.db import models
from django.contrib.auth.models import User

class CivilComplaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время обращения')
    text = models.TextField(verbose_name='Текст обращения')
    is_resolved = models.BooleanField(default=False, verbose_name='Обращение рассмотрено')

    def __str__(self):
        return f'Обращение от {self.user.username} ({self.timestamp})'

class EmployeeResponse(models.Model):
    complaint = models.OneToOneField(CivilComplaint, on_delete=models.CASCADE, related_name='response', verbose_name='Обращение')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время ответа')
    text = models.TextField(verbose_name='Текст ответа')

    def __str__(self):
        return f'Ответ на обращение от {self.complaint.user.username} ({self.timestamp})'
