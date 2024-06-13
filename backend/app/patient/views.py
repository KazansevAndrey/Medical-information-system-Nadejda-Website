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
    med_card = get_current_medcard(patient_id)
    hospitalization = get_hospitalization(med_card)
    metricks = get_metricks(med_card)
    print(med_card)
    doctor_name = get_doctor_full_name(request.user)
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
        'medcard': med_card,
        'analyzes':analyzes,
        'diagnoses':diagnoses,
        'diaries':diaries,
        'examinations':examinations
    }
    return render(request, 'basic_patient_data/medcard.html', context)


def archive_medcards_list_view(request, patient_id):
    archive_hospitalizations = get_archive_hospitalizations(patient_id)
    patient = get_patient(patient_id)
    context = {
        'archive_hospitalizations': archive_hospitalizations,
        'patient':patient,
    }
    return render(request, 'archive_medcards/archive_medcards_list.html', context=context)

def archive_medcard_view(request, patient_id, medcard_id):
    medcard = get_medcard(medcard_id)
    patient = get_patient(patient_id)
    patient_metricks = get_metricks(medcard)
    context = {
        'medcard': medcard,
        'patient':patient,
        'patient_metricks': patient_metricks
    }
    return render(request, 'archive_medcards/archive_medcard.html', context=context)

def hospitalization_info_view(request, patient_id, medcard_id=None):
    if medcard_id:
        hospitalization = get_hospitalization(medcard_id)
    else:
        medcard = get_current_medcard(patient_id)
        hospitalization = get_hospitalization(medcard)
    doctor_name = get_doctor_full_name(hospitalization.doctor_id)
    department = hospitalization.department_id
    context = {
        'hospitalization':hospitalization,
        'doctor_name':doctor_name,
        'department':department
    }
    return render(request, 'hospitalization_data/hospitalization_data.html', context)

def sorting_view(request, patient_id, list_type, category, data):
    if request.is_ajax():
        patient = get_patient(patient_id)
        med_card = get_current_medcard(patient_id)
        
        if category == "all": 
            analyzes = get_items(Analysis, med_card)
            examinations = get_items(InitialExamination, med_card)
            diagnoses = get_items(Diagnoses, med_card)
            diaries = get_items(Diarie, med_card)
        else:
            analyzes=examinations=diagnoses=diaries=None
            if category == 'analyzes':
                analyzes = get_items(Analysis, med_card)
            elif category == 'examinations':
                examinations = get_items(InitialExamination, med_card)
            elif category == 'diagnoses':
                diagnoses = get_items(Diagnoses, med_card)
            elif category == 'diaries':
                diaries = get_items(Diarie, med_card)
        
       if list_type == 'chronologically':
            pass

