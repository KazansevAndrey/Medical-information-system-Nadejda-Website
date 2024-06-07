from django.contrib import admin
from .models import Patient, AdditionalPatientMetrick, PatientMetrick, FinanceSource, Hospitalization, MedCard
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    fields = ['iin', ('first_name', 'last_name', 'surname'), 'birth_date', 'gender', 'address']
    list_filter = [("birth_date", admin.DateFieldListFilter)]

admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientMetrick)
admin.site.register(AdditionalPatientMetrick)
admin.site.register(FinanceSource)
admin.site.register(Hospitalization)
admin.site.register(MedCard)
                   

