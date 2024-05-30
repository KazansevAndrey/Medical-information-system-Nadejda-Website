from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    context = {'title': 'Главная'}
    return render(request, 'department/department.html', context)
