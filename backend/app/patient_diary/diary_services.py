import json
from .models import Diarie, DiaryType
from django.http import JsonResponse
def get_diaries(med_card):
    diaries = Diarie.objects.get(med_card=med_card)
    return diaries

def get_diary(id):
    diary = Diarie.objects.get(id=id)
    return diary

def get_diaries_types():
    diaries_types = DiaryType.objects.all()
    return diaries_types

def get_diaries_list():
    diaries_types = list(DiaryType.objects.all().values_list('name', flat=True))
    return diaries_types

def get_diary_type(diary_id):
    type = DiaryType.objects.get(id=diary_id)
    return type

def get_diary_type_by_name(name):
    diary_type = DiaryType.objects.get(name=name)
    return diary_type