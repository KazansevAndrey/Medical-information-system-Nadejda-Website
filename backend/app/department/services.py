from .models import Department
from patient.models import Patient

#Все отделения
def get_departments():
    departments = Department.objects.all()
    return departments

#Пациенты отделения
def patients_of_department(department):
    patients = Patient.objects.filter(department=department)
    return patients

 