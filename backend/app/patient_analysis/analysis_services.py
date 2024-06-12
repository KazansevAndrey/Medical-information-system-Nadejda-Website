from .models import Analysis

def get_analysis(id):
    try:
        analysis = Analysis.objects.get(id=id)
    except:
        return None
    return analysis

def get_analysis_result(analysis):
    result = analysis.results
    print(result)
    return result