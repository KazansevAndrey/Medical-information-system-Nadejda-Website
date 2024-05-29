from django.shortcuts import render

# Create your views here.
def view_department(request):
    context = {'title': 'Отделение'}
    return render(request, 'department/department.html', context)

