from django.db import models
from django.utils import timezone
from patient.models import Patient, MedCard
from accounts.models import Doctor
# Create your models here.

class DiaryType(models.Model):
    name = models.CharField(max_length=50)

class Diarie(models.Model):
    diary_type = models.ForeignKey(DiaryType, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    author = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    med_card = models.ForeignKey(MedCard, on_delete=models.CASCADE)
    bypass = models.CharField(max_length=500, null=True, blank=True) # Состав осмотра
    examination = models.CharField(max_length=500, null=True, blank=True) # Данные медицинского осмотра
    additional = models.CharField(max_length=500, null=True, blank=True) # Дополнительные сведения
    date = models.DateTimeField(default=timezone.now)
