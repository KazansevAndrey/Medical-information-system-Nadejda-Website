
from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('<str:patient_id>', views.main_data_view, name='index')
]