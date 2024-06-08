from django.shortcuts import render
from django.shortcuts import redirect
from .services import *
from accounts.doctor_services import get_doctor_full_name
from app import settings
# Create your views here.
def main_data_view(request, patient_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    patient = get_patient(patient_id)
    hospitalization = get_hospitalization_of_patient(patient_id)
    metricks = get_metricks_of_patient(patient_id)
    med_card = get_medcard(patient_id)
    doctor_name = get_doctor_full_name(request)
    department = get_department(hospitalization)
    context = {
        'doctor_name':doctor_name,
        'department':department,
        'patient': patient,
        'hospitalization': hospitalization,
        'metricks': metricks,
        'med_card': med_card,
        
    }
    return render(request, 'basic_patient_data/medcard.html', context)