from .models import Diagnoses
def get_diagnoses(med_card):
    diagnoses = Diagnoses.objects.get(med_card=med_card)
    return diagnoses