
from django.urls import path
from department import views

app_name = 'department'

urlpatterns = [
    path('<str:department_id>/', views.view_department, name='department'),
    path('<str:department_id>/fetch/', views.fetch_patients, name='fetch_patients'),
    path('<str:department_id>/search_patients/', views.search_patients, name='search')

]