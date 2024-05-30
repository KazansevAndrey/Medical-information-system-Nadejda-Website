
from django.urls import path
from department import views

app_name = 'department'

urlpatterns = [
    path('', views.view_department, name='index'),

]
