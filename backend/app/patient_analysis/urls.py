
from django.urls import path
from .views import analysis_view

app_name = 'analisys'

urlpatterns = [
    path('<int:analysis_id>',analysis_view, name='index')
]