from django.contrib import admin
from .models import *
# Register your models here.
from django.shortcuts import render

# Create your views here.
admin.site.register(AnalysisName)
admin.site.register(AnalysisIndicator)
admin.site.register(AnalysisResult)
admin.site.register(Analysis)