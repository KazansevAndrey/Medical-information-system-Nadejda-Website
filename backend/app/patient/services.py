from .models import Patient, Hospitalization, PatientMetrick, MedCard
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

def get_medcard(patient_id):
    med_card = MedCard.objects.get(patient_id=patient_id)
    return med_card

def get_department(hospitalization):
    department = hospitalization.department_id
    return department