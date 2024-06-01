import django
from django.conf import settings

# Настройка Django
django.setup()

from django.contrib.auth.models import Group

print(Group.objects.all())
Group.objects.all().delete()