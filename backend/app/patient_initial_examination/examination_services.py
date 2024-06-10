from .models import InitialExamination

def get_examinations(med_card):
    examinations = InitialExamination.objects.get(med_card=med_card)
    return examinations