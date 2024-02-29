from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class CivilComplaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата и время обращения'))
    text = models.TextField(verbose_name=_('Текст обращения'))
    is_resolved = models.BooleanField(default=False, verbose_name=_('Обращение рассмотрено'))

    def __str__(self):
        return f'{_("Обращение от")} {self.user.username} ({self.timestamp.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name = _('гражданское обращение')
        verbose_name_plural = _('гражданские обращения')
        ordering = ['-timestamp']  # Сортировка по убыванию даты и времени обращения

class EmployeeResponse(models.Model):
    complaint = models.OneToOneField(CivilComplaint, on_delete=models.CASCADE, related_name='response', verbose_name=_('Обращение'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата и время ответа'))
    text = models.TextField(verbose_name=_('Текст ответа'))

    def __str__(self):
        return f'{_("Ответ на обращение от")} {self.complaint.user.username} ({self.timestamp.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name = _('ответ сотрудника')
        verbose_name_plural = _('ответы сотрудников')
        ordering = ['-timestamp']  # Сортировка по убыванию даты и времени ответа
