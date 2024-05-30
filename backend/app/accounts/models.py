from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Department(models.Model): # Таблица отделения
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Doctor(AbstractBaseUser): # Таблица врача
    iin = models.CharField(primary_key=True, max_length=12)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=3)
    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = ['phone_number', 'position', 'department', 'code']

    def __str__(self):
        return f"{self.iin} - {self.position}"

class Patient(models.Model): # Таблица пациента
    iin = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    blood_group = models.CharField(max_length=3)
    address = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name