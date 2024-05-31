from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
@login_required
def view_department(request):
    context = {'title': 'Отделение'}
    return redirect('department:view_department')

