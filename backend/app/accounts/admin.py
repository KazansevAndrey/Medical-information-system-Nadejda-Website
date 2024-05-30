from django.contrib import admin
from .models import Doctor, Department, Patient
# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Patient)


