from django.urls import path
from .views import diagnosis_view, patient_diagnoses_view


app_name = 'diagnoses'

urlpatterns = [
    path('<int:diagnosis_id>',diagnosis_view, name='diagnosis'),
    path('list/<int:medcard_id>',patient_diagnoses_view, name='patient_diagnoses')

]