from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import DoctorManager
from department.models import Department

class Doctor(AbstractBaseUser, PermissionsMixin): # Таблица врача
    iin = models.CharField(primary_key=True, max_length=12)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT,  null=True, blank=True)
    password = models.CharField(max_length=4)
    email = models.EmailField(unique=True, null=True, blank=True)
    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = ['phone_number', 'position', 'password']
    is_staff = models.BooleanField(default=False)  # Добавление атрибута is_staff
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = DoctorManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
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