from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from app import settings

def redirect_view(request):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    else:
        print('пользователь авторизован')
        return redirect('department:department')
	
def user_login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        iin = request.POST['iin']
        code = request.POST['code']
        user = authenticate(request, username=iin, password=code, phone_number=phone_number)
        print(user)
        if user is not None:
            login(request, user)  # Аутентификация пользователя
            print("процесс аутентефикации", user.is_authenticated)
            return redirect('department:department')
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Неверные учетные данные'})
    else:
        return render(request, 'accounts/login.html')
    
def user_logout(request):
	pass