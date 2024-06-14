from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
from .services import *
from accounts.doctor_services import get_doctor_full_name
from app import settings
from patient_analysis.models import Analysis
from patient_diagnoses.models import Diagnoses
from patient_diary.models import Diarie
from patient_initial_examination.models import InitialExamination
# Create your views here.
def main_data_view(request, patient_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    
    patient = get_patient(patient_id)
    med_card = get_current_medcard(patient_id)
    hospitalization = get_hospitalization(med_card)
    metricks = get_metricks(med_card)
    print(med_card)
    doctor_name = get_doctor_full_name(request.user)
    department = get_department(hospitalization)
    analyzes = get_items(Analysis, med_card)
    examinations = get_items(InitialExamination, med_card)
    diagnoses = get_items(Diagnoses, med_card)
    diaries = get_items(Diarie, med_card)
    print(analyzes)
    
    context = {
        'doctor_name':doctor_name,
        'department':department,
        'patient': patient,
        'hospitalization': hospitalization,
        'metricks': metricks,
        'medcard': med_card,
        'analyzes':analyzes,
        'diagnoses':diagnoses,
        'diaries':diaries,
        'examinations':examinations
    }
    return render(request, 'basic_patient_data/medcard.html', context)


def archive_medcards_list_view(request, patient_id):
    archive_hospitalizations = get_archive_hospitalizations(patient_id)
    patient = get_patient(patient_id)
    context = {
        'archive_hospitalizations': archive_hospitalizations,
        'patient':patient,
    }
    return render(request, 'archive_medcards/archive_medcards_list.html', context=context)

def archive_medcard_view(request, patient_id, medcard_id):
    medcard = get_medcard(medcard_id)
    patient = get_patient(patient_id)
    patient_metricks = get_metricks(medcard)
    context = {
        'medcard': medcard,
        'patient':patient,
        'patient_metricks': patient_metricks
    }
    return render(request, 'archive_medcards/archive_medcard.html', context=context)

def hospitalization_info_view(request, patient_id, medcard_id=None):
    if medcard_id:
        hospitalization = get_hospitalization(medcard_id)
    else:
        medcard = get_current_medcard(patient_id)
        hospitalization = get_hospitalization(medcard)
    doctor_name = get_doctor_full_name(hospitalization.doctor_id)
    department = hospitalization.department_id
    context = {
        'hospitalization':hospitalization,
        'doctor_name':doctor_name,
        'department':department
    }
    return render(request, 'hospitalization_data/hospitalization_data.html', context)


def sorting_view(request, patient_id):
    if request.is_ajax():
        list_type = request.GET.get('list_type')
        category = request.GET.get('category')
        date = request.GET.get('date')
        med_card = get_current_medcard(patient_id)
        if category == "all": # Не выбрана категория. 

            if list_type == 'by_category': 
                analyzes = sorting_by_time(date, get_items(Analysis, med_card))
                examinations = sorting_by_time(date, get_items(InitialExamination, med_card))
                diagnoses = sorting_by_time(date, get_items(Diagnoses, med_card))
                diaries = sorting_by_time(date, get_items(Diarie, med_card))

                formatted_analyzes = format_items(analyzes)
                formatted_examinations = format_items(examinations)
                formatted_diagnoses = format_items(diagnoses)
                formatted_diaries = format_items(diaries)

                sent_data = {'analyzes': formatted_analyzes,
                             'analyzes_count': analyzes.count(),
                             'examinations': formatted_examinations,
                             'examinations_count':examinations.count(),
                             'diagnoses': formatted_diagnoses,
                             'diagnoses_count': diagnoses.count(),
                             'diaries':formatted_diaries,
                             'diaries_count': diaries.count()}
                print(sent_data)
            elif list_type == 'chronologically':
                items = format_items(sorting_by_time(date, get_hronologically_all_items(med_card))) # json список каждого item с нужными аттрибутами
                print(items)
                sent_data = {'items':items}
            
        else: # Выбрана конкретная категория - сортируем по хронологии 
            analyzes=examinations=diagnoses=diaries=None
            category_items = format_items(sorting_by_time(date, get_hronologically(get_items_by_category(category, med_card))))
            sent_data = {'category_items': category_items}
            
        return JsonResponse(sent_data)
        
def search_analyses_view(request, patient_id):
    query = request.GET.get('q')
    med_card = get_current_medcard(patient_id)
    analyzes = format_items(get_items(Analysis, med_card).filter(
         Q(analysis_name__name__iregex=query) | Q(analysis_name__code__iregex=query) 
    ))
    sent_data = {
        'analyzes':analyzes
    }
    return JsonResponse(sent_data)


