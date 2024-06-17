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

#Госпитализации с открытыми мед картами
def get_hospitalizations_of_department(department_id):
    hospitalizations_of_department = Hospitalization.objects.filter(med_card_id__med_card_status='o').filter(department_id=department_id)
    return hospitalizations_of_department

#Госпитализации отделения
def get_hospitalizations_of_doctor(hospitalizations_of_department, request):
    hospitalizations_of_doctor = hospitalizations_of_department.filter(doctor_id=request.user.pk)
    print("Пациенты врача: ", hospitalizations_of_doctor)
    return hospitalizations_of_doctor

#Все госпитализации с открытой мед картой
def get_all_hospitalizations():
    return Hospitalization.objects.filter(med_card_id__med_card_status='o')

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
    return patients

def get_reanimations(patients):
    reanimations = []
    for patient in patients:

        reanimation = Hospitalization.objects.get(med_card_id__med_card_status='o', patient_id=patient['id']).reanimation
        reanimations.append(reanimation)
    return reanimations