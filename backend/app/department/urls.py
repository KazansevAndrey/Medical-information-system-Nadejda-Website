
from django.urls import path
from department import views

app_name = 'department'

urlpatterns = [
    path('', views.view_department, name='department'),
    path('fetch_patients', views.fetch_patients, name='fetch_patients'),


]