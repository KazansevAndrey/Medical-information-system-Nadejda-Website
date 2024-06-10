from .models import Diarie
def get_diaries(med_card):
    diaries = Diarie.objects.get(med_card=med_card)
    return diaries