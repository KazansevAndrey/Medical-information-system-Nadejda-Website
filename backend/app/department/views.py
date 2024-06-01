from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from app import settings

# Create your views here.

def view_department(request):
    
    
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    context = {'title': 'Отделение'}
    return render(request, 'department/department.html', context)

