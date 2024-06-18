
from django.shortcuts import render
from django.shortcuts import redirect
from patient.services import get_patient_by_medcard
from .diary_services import *
from app import settings

# Create your views here.

def diary_view(request, diary_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    diary = get_diary(diary_id)
    diary_types = get_diaries_list()
    medcard = diary.med_card.id
    patient = get_patient_by_medcard(medcard)
    
    context = {
        'diary':diary,
        'patient':patient,
        'diary_types': diary_types,
        }
    
    return render(request, 'diary/diary.html', context)

def update_diary(request, diary_id):
    if request.method == 'POST':
        diary_data = json.loads(request.body)
        diary_type = get_diary_type_by_name(diary_data['diary_type'])
        # Обработка данных и сохранение в базу данных
        # Пример:
        diary = get_diary(diary_id)
        medcard_id = diary.med_card.id
        patient = get_patient_by_medcard(medcard_id)
        diary.diary_type = diary_type
        diary.patient = patient
        diary.author = request.user
        diary.bypass= diary_data['objective_data']
        diary.examination = diary_data['examination']
        diary.additional = diary_data['additional_info']
        
        diary.save()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

def delete_diary(request, diary_id):
    if request.method == 'POST':
        diary = get_diary(diary_id)
        diary.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})