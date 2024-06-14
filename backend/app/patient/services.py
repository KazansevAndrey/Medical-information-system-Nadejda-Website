from django.utils import timezone
from .models import Patient, Hospitalization, PatientMetrick, MedCard
from patient_analysis.models import Analysis
from patient_diagnoses.models import Diagnoses
from patient_diary.models import Diarie
from patient_initial_examination.models import InitialExamination
import datetime
from itertools import chain
from operator import attrgetter
from datetime import datetime, timedelta, time


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

def get_items(model, med_card): # Работает
    try:
        items = model.objects.filter(med_card=med_card)
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

def format_items(items): # Формируем json ответ для передачи в ответе ajax 
    formatted_items = []
    for item in items:
        print(item)
        if isinstance(item, Analysis):
            formatted_items.append({
                'type': 'analysis',
                'analysis_name': item.analysis_name.name,
                'date': item.date.strftime('%d.%m.%Y'),
                'id': item.id
            })
        elif isinstance(item, InitialExamination):
            formatted_items.append({
                'type': 'examination',
                'date': item.date.strftime('%d.%m.%Y'),
                'id': item.id
            })
        elif isinstance(item, Diagnoses):
            formatted_items.append({
                'type': 'diagnose',
                'code': f'({item.code.code}) {item.code.name}',
                'date': item.date.strftime('%d.%m.%Y'),
                'kind': item.get_kind_display(),
                'id': item.id
            })
        elif isinstance(item, Diarie):
            formatted_items.append({
                'type': 'diary',
                'date': item.date.strftime('%d.%m.%Y %H:%M'),
                'additional': item.additional,
                'id': item.id
            })
    return formatted_items

def get_items_by_category(category, med_card): # Работает
    item_list = []
    if category == 'analyzes':
        item_list = get_items(Analysis, med_card)
    elif category == 'examinations':
        item_list = get_items(InitialExamination, med_card)
        print('Поиск по первичному осмотру')
    elif category == 'diagnoses':
        item_list= get_items(Diagnoses, med_card)
        print('Поиск по диагнозам')
    elif category == 'diaries':
        item_list = get_items(Diarie, med_card)
    return item_list

def get_hronologically_all_items(med_card):
    # Получаем данные из каждой модели
    analyzes = Analysis.objects.filter(med_card=med_card)
    examinations = InitialExamination.objects.filter(med_card=med_card)
    diagnoses = Diagnoses.objects.filter(med_card=med_card)
    diaries = Diarie.objects.filter(med_card=med_card)

    # Объединяем все данные в один список
    combined_list = sorted(
        chain(analyzes, examinations, diagnoses, diaries),
        key=attrgetter('date'))
    return combined_list

def get_hronologically(items):
    print(items)
    combined_list = sorted(items, key=attrgetter('date')) 
    return combined_list

def sorting_by_time(period, items):
    tz = pytz.timezone('Asia/Yekaterinburg')
    if period == 'today':
        today_min = datetime.combine(timezone.now().date(), time().min)
        today_max = datetime.combine(timezone.now().date(), time().max)
        if isinstance(items, list):
            # Удаляем инфу о часовых поясах и сравниваем
            return [item for item in items if today_min.replace(tzinfo=None) <= item.date.replace(tzinfo=None) <= today_max.replace(tzinfo=None)] 
        return items.filter(date__range=(today_min, today_max))
    elif period == 'yesterday':
        yesterday = timezone.now().date() - timedelta(days=1)
        yesterday_max = datetime.combine(yesterday, time.max) 
        yesterday_min = datetime.combine(yesterday, time.min) 
        if isinstance(items, list):
            return [item for item in items if today_min.replace(tzinfo=None) <= item.date.replace(tzinfo=None) <= today_max.replace(tzinfo=None)] 

        return items.filter(date__range=(yesterday_min, yesterday_max))
    
    elif period == 'last_2_days':
        yesterday = timezone.now().date()-timedelta(days=1)
        yesterday_min = datetime.combine(yesterday, time.min) 
        today_max = datetime.combine(timezone.now().date(), time().max)
        return items.filter(date__range=(yesterday_min, today_max))

    else:
        return items
    
