from .models import InitialExamination

def get_examination(id):
    examinations = InitialExamination.objects.get(id=id)
    return examinations
