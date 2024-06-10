from django.shortcuts import render
from django.shortcuts import redirect
from .services import *
from accounts.doctor_services import get_doctor_full_name
from app import settings
from patient_analysis.models import Analysis
from patient_diagnoses.models import Diagnoses
from patient_diary.models import Diarie
from patient_initial_examination.models import InitialExamination
# Create your views here.
def main_data_view(request, patient_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    patient = get_patient(patient_id)
    hospitalization = get_hospitalization_of_patient(patient_id)
    metricks = get_metricks_of_patient(patient_id)
    med_card = get_current_medcard(patient_id)
    print(med_card)
    doctor_name = get_doctor_full_name(request)
    department = get_department(hospitalization)
    analyzes = get_items(Analysis, med_card)
    examinations = get_items(InitialExamination, med_card)
    diagnoses = get_items(Diagnoses, med_card)
    diaries = get_items(Diarie, med_card)
    print(analyzes)
    
    context = {
        'doctor_name':doctor_name,
        'department':department,
        'patient': patient,
        'hospitalization': hospitalization,
        'metricks': metricks,
        'med_card': med_card,
        'analyzes':analyzes,
        'diagnoses':diagnoses,
        'diaries':diaries,
        'examinations':examinations
    }
    return render(request, 'basic_patient_data/medcard.html', context)