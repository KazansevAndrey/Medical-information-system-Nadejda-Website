from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import DoctorManager
from department.models import Department

class Doctor(AbstractBaseUser, PermissionsMixin): # Таблица врача
    iin = models.CharField(primary_key=True, max_length=12)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department, related_name='doctors', blank=True)
    password = models.CharField(max_length=4)
    first_name = models.CharField(max_length=20, default='Имя')
    last_name = models.CharField(max_length=20, default='Фамилия')
    email = models.EmailField(unique=True, null=True, blank=True)
    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = ['phone_number', 'password', 'first_name', 'last_name', 'position']
    is_staff = models.BooleanField(default=False)  # Добавление атрибута is_staff
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = DoctorManager()

    

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
        return f"{self.name}"