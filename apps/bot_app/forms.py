from django import forms
from .models import CivilComplaint, EmployeeResponse

class CivilComplaintForm(forms.ModelForm):
    class Meta:
        model = CivilComplaint
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваше обращение здесь...'}),
        }

class EmployeeResponseForm(forms.ModelForm):
    class Meta:
        model = EmployeeResponse
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваш ответ здесь...'}),
        }
