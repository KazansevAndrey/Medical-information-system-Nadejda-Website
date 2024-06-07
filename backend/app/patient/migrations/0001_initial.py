# Generated by Django 4.2.13 on 2024-06-07 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalPatientMetrick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(default='-', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('Ж', 'Женщина')], max_length=1)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PatientMetrick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('temperatury', models.CharField(max_length=4)),
                ('puls', models.CharField(max_length=4)),
                ('resperatory_rate', models.CharField(max_length=3)),
                ('pressure', models.CharField(max_length=7)),
                ('saturation', models.CharField(max_length=3)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_card_number', models.CharField(max_length=4)),
                ('med_card_status', models.CharField(choices=[('o', 'Открыта'), ('c', 'Закрыта')], max_length=7)),
                ('additional_patient_metrick', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.additionalpatientmetrick')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('patient_metrick', models.ForeignKey(default='-', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.patientmetrick')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalization_type', models.CharField(choices=[('E', 'Экстренное (Первые 6 часов)'), ('M', 'Первые 24 часа'), ('P', 'Плановое')], default='M', max_length=1)),
                ('reanimation', models.BooleanField()),
                ('receipt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_of_discharge', models.DateTimeField(blank=True, null=True)),
                ('department_id', models.ForeignKey(default='-', null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department')),
                ('doctor_id', models.ForeignKey(default='-', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('finance_source_id', models.ForeignKey(default='-', null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.financesource')),
                ('med_card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.medcard')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
        migrations.AddField(
            model_name='additionalpatientmetrick',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
