from .models import Patient, Hospitalization, PatientMetrick, MedCard
from patient_analysis.models import Analysis
import datetime

def get_patient(patient_id):
    patient = Patient.objects.get(id=patient_id)
    return patient

def get_patient_by_medcard(medcard_id):
    medcard = MedCard.objects.get(id=medcard_id)
    patient = medcard.patient
    return patient

def get_medcard(medcard_id):
    med_card = MedCard.objects.get(id=medcard_id)
    return med_card

def get_current_medcard(patient_id):
    med_card = MedCard.objects.filter(med_card_status='o').get(patient_id=patient_id)
    return med_card

def get_hospitalization(medcard):
    try:
        hospitalization = Hospitalization.objects.get(med_card_id=medcard)
    except Hospitalization.DoesNotExist:
        return None  # Или выбросьте свое исключение, или обработайте иначе
    return hospitalization

def get_metricks(medcard):
    metricks = PatientMetrick.objects.get(med_card=medcard.id)
    return metricks

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

def get_archive_medcards(patient_id):
    archive_medcards = MedCard.objects.filter(patient=patient_id).filter(med_card_status='c')
    return archive_medcards

def get_archive_hospitalizations(patient_id):
    archive_medcards = MedCard.objects.filter(patient=patient_id).filter(med_card_status='c').values_list('id', flat=True)
    hospitalizations = Hospitalization.objects.filter(med_card_id__in=archive_medcards)
    return hospitalizations
