from .models import Department
from patient.models import Patient, MedCard, Hospitalization

#Все отделения
def get_departments():
    departments = Department.objects.all()
    return departments

#Первое отделение
def get_first_department():
    first_department = Department.objects.all()[0]
    return first_department

#Пациенты отделения
def get_hospitalizations_of_department(department_id):
    hospitalizations_of_department = Hospitalization.objects.filter(department_id=department_id)
    return hospitalizations_of_department

#Пациенты врача
def get_hospitalizations_of_doctor(patients, request):
    hospitalizations_of_doctor = Hospitalization.objects.filter(doctor_id=request.user.pk)

   
    print("Пациенты врача: ", hospitalizations_of_doctor)
    return hospitalizations_of_doctor

#Все пациеты
def get_all_hospitalizations():
    return Hospitalization.objects.all()

def get_patients(hospitalizations):
    patients = []
    for hospitalization in hospitalizations:
        patients.append({
            'id': hospitalization.patient_id.id,
            'last_name': hospitalization.patient_id.last_name,
            'first_name': hospitalization.patient_id.first_name,
            'surname': hospitalization.patient_id.surname,
            'age': hospitalization.patient_id.age,
            'receipt_date': hospitalization.receipt_date.strftime("%d.%m.%Y %H:%M"),
        })
        print('Пациенты ....', patients)
    return patients