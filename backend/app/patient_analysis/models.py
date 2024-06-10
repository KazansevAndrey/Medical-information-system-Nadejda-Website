from django.db import models
# Create your models here.
from django.db import models
from patient.models import Patient, MedCard

# Create your models here.
'''Модели анализов'''

class AnalysisName(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=11)
    def __str__(self):
        return self.name

class AnalysisIndicator(models.Model):
    analysis_name = models.ForeignKey(AnalysisName, on_delete=models.CASCADE)
    indicator_name = models.CharField(max_length=50)
    indicator_norm = models.CharField(max_length=50, null=True, blank=True)
    indicator_unit = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return f'{self.analysis_name}- {self.indicator_name} Норма: {self.indicator_norm}'
    
class Analysis(models.Model):
    analysis_name = models.ForeignKey(AnalysisName, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med_card = models.ForeignKey(MedCard, on_delete=models.CASCADE)
    date_taken = models.DateTimeField()
    status_choices = [
        ('Принят на работу', 'Pending'),
        ('Завершен', 'Completed'),
    ]
    status = models.CharField(max_length=16, choices=status_choices, default='pending')

    @property
    def results(self):
        results = []
        query = AnalysisResult.objects.filter(analysis=self).select_related('analysis_indicator')
        for result in query:
            results.append({
                'indicator': result.analysis_indicator.indicator_name,
                'result': result.analysis_result,
                'norm': result.analysis_indicator.indicator_norm,
                'unit': result.analysis_indicator.indicator_unit,
            })
        return results        
    
    def __str__(self):
        return f'{self.patient} - {self.analysis_name} Дата взятия: {self.date_taken}'


class AnalysisResult(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    analysis_indicator = models.ForeignKey(AnalysisIndicator, on_delete=models.CASCADE)
    analysis_result = models.CharField(max_length=50)

    class Meta:
        unique_together = ('analysis', 'analysis_indicator') # Что бы к одному анализу один индикатор

    def __str__(self):
        return f'{self.analysis_indicator} Результат: {self.analysis_result}'
