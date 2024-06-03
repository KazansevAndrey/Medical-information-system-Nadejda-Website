from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import json
from accounts import doctor_services
from app import settings
from .services import *
# Create your views here.

def view_department(request):
    
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    departments = get_departments()
    first_department_id = get_first_department().pk
    patients_of_department = get_patients_of_department(first_department_id)
    
    print(departments)
    doctor_name = doctor_services.get_doctor_full_name(request)
    context = {
        'departments':departments,
        'patients_of_department': patients_of_department,
        'title': 'Отделение',
        'doctor_name':doctor_name, 
        
    }
    return render(request, 'department/department.html', context)

def fetch_patients(request):
    if request.is_ajax():
        department_id = request.GET.get('department_id')
        patients_list = get_patients_of_department(department_id)
        data = []
        for patient in patients_list:
            data.append({
                'last_name': patient.last_name,
                'first_name': patient.first_name,
                'surname': patient.surname,
                'age': patient.age,
                'receipt_date': patient.receipt_date.strftime("%d.%m.%Y %H:%M"),
        })
        data = JSON.parse(data);

        sent_data = {'patient_list': data}
        return JsonResponse(sent_data)