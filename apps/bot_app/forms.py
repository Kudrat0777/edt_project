from django import forms
from .models import CivilComplaint, EmployeeResponse
from django.utils.translation import gettext_lazy as _

class CivilComplaintForm(forms.ModelForm):
    class Meta:
        model = CivilComplaint
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': _('Введите ваше обращение здесь...'), 'class': 'form-control'}),
        }
        labels = {
            'text': _('Текст обращения'),
        }

class EmployeeResponseForm(forms.ModelForm):
    class Meta:
        model = EmployeeResponse
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': _('Введите ваш ответ здесь...'), 'class': 'form-control'}),
        }
        labels = {
            'text': _('Текст ответа'),
        }
