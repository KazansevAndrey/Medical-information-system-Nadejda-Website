
from django.urls import path
from department import views

app_name = 'department'

urlpatterns = [
    path('', views.view_department, name='department'),
    path('selected_department', views.view_selected_department, name='selected_dep')
]