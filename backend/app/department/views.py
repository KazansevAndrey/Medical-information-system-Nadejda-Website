from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from accounts import doctor_services
from django.http import JsonResponse
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

def view_selected_department(request, department_id):
    if request.is_ajax():
        patients_of_department = get_patients_of_department(department_id)
        patient_serializers = serializers.serialize('json', patients_of_department)
        return JsonResponse({patient_serializers})

