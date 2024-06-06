from .models import Department
from patient.models import Patient

#Все отделения
def get_departments():
    departments = Department.objects.all()
    return departments

#Первое отделение
def get_first_department():
    first_department = Department.objects.all()[0]
    return first_department

#Пациенты отделения
def get_patients_of_department(department_id):
    patients = Patient.objects.filter(department_id=department_id)
    print(f"Пациенты отделения {department_id}", patients)
    return patients

#Пациенты врача
def get_patients_of_doctor(patients, request):
    print("Пациенты врача: ", patients.filter(doctor=request.user.pk))
    return patients.filter(doctor=request.user.pk)

#Все пациеты
def get_all_patients():
    return Patient.objects.all()
