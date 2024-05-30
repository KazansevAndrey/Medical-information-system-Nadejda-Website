from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def redirect_view(request):
	return redirect('/department')
	
def user_login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        iin = request.POST['iin']
        code = request.POST['code']
        user = authenticate(request, username=iin, phone_number=phone_number, password=code)
        print(user)
        if user is not None:
            login(request, user)  # Аутентификация пользователя
            return redirect('department:redirect')
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Неверные учетные данные'})
    else:
        return render(request, 'accounts/login.html')
def user_logout(request):
	pass