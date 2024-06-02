from .models import Department
from patient.models import Patient

#Все отделения
def get_departments():
    departments = Department.objects.all()
    return departments

#Пациенты отделения
def get_patients_of_department(department_id):
    patients = Patient.objects.filter(department_id=department_id)
    return patients

 