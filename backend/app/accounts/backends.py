from django.contrib.auth.backends import BaseBackend
from .models import Doctor

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, iin=None, phone_number=None, code=None):
        try:
            doctor = Doctor.objects.get(iin=iin, phone_number=phone_number, code=code)
            return doctor
        except Doctor.DoesNotExist:
            return None
