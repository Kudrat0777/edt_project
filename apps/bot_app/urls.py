from django.urls import path
from .views import complaint_list, submit_complaint, respond_to_complaint


app_name = 'bot_app'


urlpatterns = [
    path('complaints/', complaint_list, name='complaint_list'),
    path('submit_complaint/', submit_complaint, name='submit_complaint'),
    path('respond_to_complaint/<int:complaint_id>/', respond_to_complaint, name='respond_to_complaint'),
]