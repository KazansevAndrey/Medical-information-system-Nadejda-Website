from django.contrib.auth.backends import BaseBackend
from .models import Doctor
from django.core.exceptions import ObjectDoesNotExist

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, phone_number=None, password=None):
        try:
            print('Отработка проверки')
            doctor = Doctor.objects.get(iin=username, phone_number=phone_number, password=password)
            if doctor is not None:
                return doctor
            else:
                return None
        except ObjectDoesNotExist:
            return None
