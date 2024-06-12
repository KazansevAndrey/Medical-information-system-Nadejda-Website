from django.shortcuts import render
from django.shortcuts import redirect
from app import settings
from .examination_services import *
from patient.services import get_patient_by_medcard

# Create your views here.
def examination_view(request, examination_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    examination = get_examination(examination_id)
    medcard = examination.med_card.id
    patient = get_patient_by_medcard(medcard)
    context = {
        'examination':examination,
        'patient':patient,
        }
    
    return render(request, 'initial_examination/initial_examination.html', context)