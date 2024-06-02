'''Модель Отделения'''

from django.db import models

# Create your models here.
class Department(models.Model): # Таблица отделения
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"
    

