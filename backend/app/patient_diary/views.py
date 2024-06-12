
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
    print(diary)
    medcard = diary.med_card.id
    patient = get_patient_by_medcard(medcard)
    
    context = {
        'diary':diary,
        'patient':patient,
        }
    
    return render(request, 'diary/diary.html', context)
