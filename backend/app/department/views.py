from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q
import json
from accounts import doctor_services
from django.http import JsonResponse
from app import settings
from .services import *
from django.views.generic.list import ListView
# Create your views here.

def view_department(request, department_id):
    
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    departments = get_departments()
    doctor_name = doctor_services.get_doctor_full_name(request)

    if department_id == 'all':
        hospitalizations_of_department = get_all_hospitalizations()
        hospitalizations_of_doctor = get_hospitalizations_of_doctor(hospitalizations_of_department, request)
        current_department_id = 'all'
    else:
        hospitalizations_of_department = get_hospitalizations_of_department(department_id)
        hospitalizations_of_doctor = get_hospitalizations_of_doctor(hospitalizations_of_department, request)
        current_department_id = int(department_id)
        print(hospitalizations_of_doctor, "пациенты доктора")
    context = {
        'current_department_id': current_department_id,
        'departments':departments,
        'hospitalizations_of_department': hospitalizations_of_department,
        'title': 'Отделение',
        'doctor_name':doctor_name,
        'hospitalizations_of_doctor':hospitalizations_of_doctor,
    }
    return render(request, 'department/department.html', context)

def fetch_patients(request, department_id):
    if request.is_ajax():
        if department_id == 'all':
            hospitalizations_of_department = get_all_hospitalizations()
            hospitalizations_of_doctor = get_hospitalizations_of_doctor(hospitalizations_of_department, request)
        else:
            hospitalizations_of_department = get_hospitalizations_of_department(department_id)
            hospitalizations_of_doctor = get_hospitalizations_of_doctor(hospitalizations_of_department, request)

        department_patients = []
        doctor_patients = []
        department_patients = get_patients(hospitalizations_of_department)
        doctor_patients = get_patients(hospitalizations_of_doctor)
        sent_data = {'patients_of_department': department_patients, 'patients_of_doctor': doctor_patients}
        return JsonResponse(sent_data)
    
def search_patients(request, department_id): 
    if request.is_ajax():
        query = request.GET.get('q')
        if department_id == 'all':
            hospitalizations_of_department = get_all_hospitalizations()
            hospitalizations_of_doctor = get_hospitalizations_of_doctor(hospitalizations_of_department, request) 
        else:      
            hospitalizations_of_department = get_hospitalizations_of_department(department_id)
            hospitalizations_of_doctor = get_hospitalizations_of_doctor(hospitalizations_of_department, request)
        hospitalizations_of_department = hospitalizations_of_department.filter(
            Q(patient_id__first_name__iregex=query) | Q(patient_id__last_name__iregex=query) | Q(patient_id__surname__iregex=query)
        )
        hospitalizations_of_doctor = hospitalizations_of_doctor.filter(
            Q(patient_id__first_name__iregex=query) | Q(patient_id__last_name__iregex=query) | Q(patient_id__surname__iregex=query)
        )
        
        department_patients = []
        doctor_patients = []
        department_patients = get_patients(hospitalizations_of_department)
        doctor_patients = get_patients(hospitalizations_of_doctor)      
        sent_data = {'patients_of_department': department_patients, 'patients_of_doctor': doctor_patients}
        return JsonResponse(sent_data)
    

