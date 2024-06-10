from django.db import models
from patient.models import Patient, MedCard
from accounts.models import Doctor
from django.utils import timezone
# Create your models here.

class DiagnosesName(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=7)
    def __str__(self):
        return f'({self.code}) {self.name}'

class Diagnoses(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    author = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True )
    med_card = models.ForeignKey(MedCard, on_delete=models.CASCADE, null=True)
    code = models.ForeignKey(DiagnosesName, on_delete=models.CASCADE)
    kind_choices = [('p', 'Предварительный'), ('c', 'Клинический'), ('f', 'Окончательный')]
    kind = models.CharField(max_length=1, choices=kind_choices, null=True, blank=True)
    type_choices = [('main', 'Основное'), ('сopg', 'Конкурирующее'), ('back', 'Фоновое'), ('copn', 'Осложнение')]
    types = models.CharField(max_length=4, choices=type_choices, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.code} - {self.patient}'