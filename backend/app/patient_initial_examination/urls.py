
from django.urls import path
from .views import examination_view

app_name = 'examination'

urlpatterns = [
    path('<int:examination_id>', examination_view, name='index')
]