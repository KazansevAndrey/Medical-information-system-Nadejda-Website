from .models import Diarie
def get_diaries(med_card):
    diaries = Diarie.objects.get(med_card=med_card)
    return diaries

def get_diary(id):
    diary = Diarie.objects.get(id=id)
    return diary