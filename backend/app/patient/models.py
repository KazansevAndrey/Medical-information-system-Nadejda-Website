from django.db import models
from django.utils import timezone
from department.models import Department
from accounts.models import Doctor
from datetime import date
# Create your models here.
class Patient(models.Model): # Таблица пациента
    iin = models.CharField(max_length=12)
    first_name = models.CharField(max_length=20, )
    last_name = models.CharField(max_length=20, )
    surname = models.CharField(max_length=20, )
    birth_date = models.DateField()
    gender_choices = [
        ('M', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    address = models.CharField(max_length=200)
    
    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"
    
class PatientMetrick(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    temperatury = models.CharField(max_length=4)
    puls = models.CharField(max_length=4)
    resperatory_rate = models.CharField(max_length=3)
    pressure = models.CharField(max_length=7)
    saturation = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.patient} Рост {self.height}. Вес {self.weight}кг"

class AdditionalPatientMetrick(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    value = models.CharField(max_length=10, default='-')
    
    def __str__(self):
        return f"{self.name} - {self.value}"
    
class FinanceSource(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    
class MedCard(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_metrick = models.ForeignKey(PatientMetrick, on_delete=models.SET_NULL, null=True)
    additional_patient_metrick = models.ForeignKey(AdditionalPatientMetrick, on_delete=models.SET_NULL, null=True, blank=True)
    med_card_number = models.CharField(max_length=4)
    med_card_status_choices = [
        ('o', 'Открыта'),
        ('c','Закрыта'),
    ]
    med_card_status = models.CharField(max_length=7, choices=med_card_status_choices)
    
    def __str__(self):
        return f"{self.med_card_number} {self.patient}"

class Hospitalization(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med_card_id = models.ForeignKey(MedCard, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    finance_source_id = models.ForeignKey(FinanceSource, on_delete=models.SET_NULL, null=True, blank=True)
    hospitalization_choices = [('E', 'Экстренное (Первые 6 часов)'), ('M', "Первые 24 часа"), ('P', 'Плановое')]
    hospitalization_type = models.CharField(max_length=1, choices=hospitalization_choices, default='M')
    reanimation = models.BooleanField()
    receipt_date = models.DateTimeField(default=timezone.now)
    date_of_discharge = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.patient_id} {self.department_id}"