
from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('<str:patient_id>', views.main_data_view, name='index'),
    path('<str:patient_id>/sorting', views.sorting_view, name='sorting'),
    path('<str:patient_id>/search_analyses', views.search_analyses_view, name='search_analyses'),
    path('<str:patient_id>/archive_medcards', views.archive_medcards_list_view, name='archive_medcards'),
    path('<str:patient_id>/archive_medcards/<str:medcard_id>', views.archive_medcard_view, name='archive_medcards'),
    path('<str:patient_id>/hospitalization_info', views.hospitalization_info_view, name='archive_medcards'),
    path('<str:patient_id>/archive_medcards/<str:medcard_id>/hospitalization_info', views.hospitalization_info_view, name='archive_medcards'),

]