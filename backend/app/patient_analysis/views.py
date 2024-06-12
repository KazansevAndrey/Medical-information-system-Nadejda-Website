from django.shortcuts import render
from django.shortcuts import redirect
from .analysis_services import *
from patient.services import get_patient_by_medcard
from accounts.doctor_services import get_doctor_full_name
from app import settings
from patient_analysis.models import Analysis
from patient_diagnoses.models import Diagnoses
from patient_diary.models import Diarie
from patient_initial_examination.models import InitialExamination
# Create your views here.

def analysis_view(request, analysis_id):
    if not request.user.is_authenticated:
        print('пользователь не авторизован')
        return redirect(settings.LOGIN_URL)
    analysis = get_analysis(analysis_id)
    medcard = analysis.med_card.id
    patient = get_patient_by_medcard(medcard)
    result = get_analysis_result(analysis)
    context = {
        'analysis':analysis,
        'patient':patient,
        'result': result}
    
    return render(request, 'analysis/analysis.html', context)