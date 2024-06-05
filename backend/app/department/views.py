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

def view_department(request):
    
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    departments = get_departments()
    first_department_id = get_first_department().pk
    patients_of_department = get_patients_of_department(first_department_id)
    patients_of_doctor = get_patients_of_doctor(patients_of_department, request)
    print(patients_of_doctor, "пациенты доктора")
    doctor_name = doctor_services.get_doctor_full_name(request)
    context = {
        'departments':departments,
        'patients_of_department': patients_of_department,
        'title': 'Отделение',
        'doctor_name':doctor_name,
        'patients_of_doctor':patients_of_doctor,
    }
    return render(request, 'department/department.html', context)

def fetch_patients(request):
    if request.is_ajax():
        department_id = request.GET.get('department_id')
        patients_of_department = get_patients_of_department(department_id)
        patients_of_doctor = get_patients_of_doctor(patients_of_department, request)
        department_patients = []
        doctor_patients = []
        for patient in patients_of_department:
            department_patients.append({
                'last_name': patient.last_name,
                'first_name': patient.first_name,
                'surname': patient.surname,
                'age': patient.age,
                'receipt_date': patient.receipt_date.strftime("%d.%m.%Y %H:%M"),
        })
        
        for patient in patients_of_doctor:
            doctor_patients.append({
                'last_name': patient.last_name,
                'first_name': patient.first_name,
                'surname': patient.surname,
                'age': patient.age,
                'receipt_date': patient.receipt_date.strftime("%d.%m.%Y %H:%M"),
        })
            
        sent_data = {'patients_of_department': department_patients, 'patients_of_doctor': doctor_patients}
        return JsonResponse(sent_data)
    

 
def search_patients(request): # новый
    print("ХУЙ")
    department_id = request.GET.get('department_id')
    print(department_id)
    patients_of_department = get_patients_of_department(department_id)
    patients_of_doctor = get_patients_of_doctor(patients_of_department, request)
    query = request.GET.get('q')
    department_patients = patients_of_department.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(surname__icontains=query)
    )
    doctor_patients = patients_of_doctor.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(surname__icontains=query)
    )

    sent_data = {'patients_of_department': department_patients, 'patients_of_doctor': doctor_patients}
    return render(request, 'department/department.html', sent_data)
