# Generated by Django 4.2.13 on 2024-06-08 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisindicator',
            name='analysis_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients_analysis.analysisname'),
            preserve_default=False,
        ),
    ]
