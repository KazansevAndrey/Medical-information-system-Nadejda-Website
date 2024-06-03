from django.db import models
from django.utils import timezone
from department.models import Department
from accounts.models import Doctor
from datetime import date
# Create your models here.
class Patient(models.Model): # Таблица пациента
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    iin = models.CharField(primary_key=True, max_length=12)
    first_name = models.CharField(max_length=20, )
    last_name = models.CharField(max_length=20, )
    surname = models.CharField(max_length=20, )
    birth_date = models.DateField()
    receipt_date = models.DateTimeField(default=timezone.now)
    gender_choices = [
        ('M', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    address = models.CharField(max_length=200)
    med_card_status_choices = [
        ('o', 'Открыта'),
        ('c','Закрыта'),
    ]
    med_card_status = models.CharField(max_length=7, choices=med_card_status_choices)
    med_card_number = models.CharField(max_length=4)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    temperatury = models.CharField(max_length=4)
    puls = models.CharField(max_length=4)
    resperatory_rate = models.CharField(max_length=3)
    pressure = models.CharField(max_length=7)
    saturation = models.CharField(max_length=3)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"
    
class AdditionalPatientMetrick(models.Model):
    patient = models.ForeignKey(Patient, related_name='Additional_patient_metrick', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    value = models.CharField(max_length=10, default='-')
    
    def __str__(self):
        return f"{self.name} - {self.value}"
    