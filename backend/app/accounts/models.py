from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import DoctorManager
from department.models import Department

class Doctor(AbstractBaseUser, PermissionsMixin): # Таблица врача
    iin = models.CharField(primary_key=True, max_length=12)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    password = models.CharField(max_length=4)
    first_name = models.CharField(max_length=20,)
    last_name = models.CharField(max_length=20,)
    surname = models.CharField(max_length=20,)
    email = models.EmailField(unique=True, null=True, blank=True)
    USERNAME_FIELD = 'iin'
    REQUIRED_FIELDS = ['phone_number', 'password', 'first_name', 'last_name', 'surname', 'position']
    is_staff = models.BooleanField(default=False)  # Добавление атрибута is_staff
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = DoctorManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"

