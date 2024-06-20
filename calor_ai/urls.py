from django.urls import path
from . import api

urlpatterns = [
    path('api/analyze/', api.upload_and_analyze, name='analyze-food'),
    path('api/daily/', api.daily_report, name='daily-report'),
    path('api/weekly/', api.weekly_report, name='weekly-report'),
]