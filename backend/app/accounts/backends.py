from django.contrib.auth.backends import BaseBackend
from .models import Doctor
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username, phone_number, password):
        print(Doctor.objects.all())
        try:
            
            doctor = Doctor.objects.get(iin=username, phone_number=phone_number, password=password)
            
            if doctor is not None:
                
                return doctor
            else:
                return None
        except ObjectDoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return Doctor.objects.get(pk=user_id)
        except Doctor.DoesNotExist:
            return None

class CustomAdminBackend(BaseBackend):
    def authenticate(self, request, username,  password):

        try:
            doctor = Doctor.objects.get(iin=username)
            if doctor is not None and check_password(password, doctor.password):
                return doctor
            else:
                return None
        except ObjectDoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return Doctor.objects.get(pk=user_id)
        except Doctor.DoesNotExist:
            return None