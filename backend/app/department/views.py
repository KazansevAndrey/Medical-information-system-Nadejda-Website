from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from accounts import doctor_services
from app import settings
from .services import get_departments, get_patients_of_department
# Create your views here.

def view_department(request):
    
    
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    departments = get_departments()
    patients = get_patients_of_department()
    print(departments)
    doctor_name = doctor_services.get_doctor_full_name(request)
    context = {'title': 'Отделение', 'doctor_name':doctor_name, 'departments':departments}
    return render(request, 'department/department.html', context)

