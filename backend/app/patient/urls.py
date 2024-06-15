
from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('<str:patient_id>', views.main_data_view, name='index'),
    path('<str:patient_id>/sorting', views.sorting, name='sorting'),
    path('<str:patient_id>/updatePatientData', views.update_patient_data, name='update_patient_data'),
    path('<str:patient_id>/add-diary', views.add_diary, name='update_patient_data'),
    path('<str:patient_id>/search_analyses', views.search_analyses, name='search_analyses'),
    path('<str:patient_id>/archive_medcards', views.archive_medcards_list_view, name='archive_medcards'),
    path('<str:patient_id>/archive_medcards/<str:medcard_id>', views.archive_medcard_view, name='archive_medcards'),
    path('<str:patient_id>/hospitalization_info', views.hospitalization_info_view, name='archive_medcards'),
    path('<str:patient_id>/archive_medcards/<str:medcard_id>/hospitalization_info', views.hospitalization_info_view, name='archive_medcards'),

]