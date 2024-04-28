from django.urls import path
from . import api
from .api import DietPlanAPIView,suggest_diet_plan

urlpatterns = [
    path('api/dietplans/', DietPlanAPIView.as_view(), name='dietplan-list'),
    path('api/suggest/', api.suggest_diet_plan, name='suggest-dietplan'),
]
