from .models import Analysis

def get_analysis(id):
    try:
        analysis = Analysis.objects.get(id=id)
    except:
        return None
    return analysis

def get_patient_of_analysis(analysis):
    patient = analysis.patient
    return patient

def get_analysis_result(analysis):
    result = analysis.results
    print(result)
    return result