from django.contrib import admin
from .models import Patient, AdditionalPatientMetrick
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    fields = ['doctor', 'department', 'iin', ('first_name', 'last_name', 'surname'), ('birth_date', 'receipt_date'), 'gender', 'address', ('med_card_status', 'med_card_number'), ('height', 'weight'), 'temperatury', 'resperatory_rate', 'pressure', 'saturation']
    list_filter = [("birth_date", admin.DateFieldListFilter)]

admin.site.register(Patient, PatientAdmin)

admin.site.register(AdditionalPatientMetrick)