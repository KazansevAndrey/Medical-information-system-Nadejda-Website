from .models import Diarie, DiaryType
def get_diaries(med_card):
    diaries = Diarie.objects.get(med_card=med_card)
    return diaries

def get_diary(id):
    diary = Diarie.objects.get(id=id)
    return diary

def get_diaries_types():
    diaries_types = DiaryType.objects.all()
    return diaries_types

def get_diary_type(diary_id):
    type = DiaryType.objects.get(id=diary_id)
    return type