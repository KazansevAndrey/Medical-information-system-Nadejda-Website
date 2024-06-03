from .models import Department
from patient.models import Patient

#Все отделения
def get_departments():
    departments = Department.objects.all()
    return departments

def get_first_department():
    first_department = Department.objects.all()[0]
    return first_department

#Пациенты отделения
def get_patients_of_department(department_id):
    patients = Patient.objects.filter(department_id=department_id)
    print(f"Пациенты отделения {department_id}", patients)
    return patients

#Склонение возраста
def age_pluralize(age):
    if   age[-1] in '1':
            return('год')
    elif age[-1] in '234':
        return('года')
    else:
            return('лет')
 