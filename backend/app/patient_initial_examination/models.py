from django.db import models
from patient.models import Patient, MedCard
from accounts.models import Doctor
# Create your models here.
class InitialExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    author = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    med_card = models.ForeignKey(MedCard, on_delete=models.CASCADE)
    bypass = models.CharField(max_length=500, null=True, blank=True) # Состав осмотра
    complaints = models.CharField(max_length=500, null=True, blank=True) # Жалобы больного
    medical_history = models.CharField(max_length=500, null=True, blank=True) # Анамнез заболевания
    anamnesis_of_life = models.CharField(max_length=500, null=True, blank=True) # Анамнез жизни
    allergic_history = models.CharField(max_length=500, null=True, blank=True) # Аллергический анамнез
    transfusion_history = models.CharField(max_length=500, null=True, blank=True) # Трансфизионный анамнез
    objective_examination_data = models.CharField(max_length=500, null=True, blank=True) # Данные объективного осмотра
    is_examined_on_an_outpatient_basis = models.BooleanField(default=False)
    examination_plan = models.CharField(max_length=500, null=True, blank=True)
    treatment_plan = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Initial Examination of {self.patient}"
