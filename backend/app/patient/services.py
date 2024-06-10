from .models import Patient, Hospitalization, PatientMetrick, MedCard
from patient_analysis.models import Analysis
import datetime

def get_patient(patient_id):
    patient = Patient.objects.get(id=patient_id)
    return patient

def get_hospitalization_of_patient(patient_id):
    hospitalization = Hospitalization.objects.get(patient_id=patient_id)
    return hospitalization

def get_metricks_of_patient(patient_id):
    metricks = PatientMetrick.objects.get(patient_id=patient_id)
    return metricks

def get_current_medcard(patient_id):
    med_card = MedCard.objects.filter(med_card_status='o').get(patient_id=patient_id)
    return med_card

def get_department(hospitalization):
    department = hospitalization.department_id
    return department

def get_items(model, med_card):
    try:
        items = model.objects.filter(med_card=med_card)
        print(items)
    except:
        return model.objects.none()
    return items

