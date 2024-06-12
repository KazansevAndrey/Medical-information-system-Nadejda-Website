from django.shortcuts import render
from django.shortcuts import redirect
from patient.services import get_patient_by_medcard
from .diagnoses_services import *
from accounts.doctor_services import get_doctor_full_name
from app import settings

# Create your views here.

def diagnosis_view(request, diagnosis_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    diagnosis = get_diagnosis(diagnosis_id)
    medcard = diagnosis.med_card.id
    patient = get_patient_by_medcard(medcard)
    
    context = {
        'diagnosis':diagnosis,
        'patient':patient,
        }
    
    return render(request, 'diagnoses/diagnosis.html', context)

def patient_diagnoses_view(request, medcard_id):
    diagnoses = get_diagnoses(medcard_id)
    patient = get_patient_by_medcard(medcard_id)
    context = {
        'diagnoses': diagnoses,
        'patient':patient
    }
    return render(request, 'diagnoses/patient_diagnoses.html', context)