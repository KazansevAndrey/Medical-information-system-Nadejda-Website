from django.contrib import admin
from .models import Doctor
# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class DoctorAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name', 'surname'), 'iin', 'phone_number', 'password', 'email', 'position']

admin.site.register(Doctor, DoctorAdmin)



