from .models import Diagnoses
def get_diagnoses(med_card):
    diagnoses = Diagnoses.objects.filter(med_card=med_card)
    return diagnoses

def get_diagnosis(id):
    diagnosis = Diagnoses.objects.get(id=id)
    return diagnosis

