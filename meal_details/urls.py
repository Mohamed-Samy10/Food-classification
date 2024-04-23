from django.urls import path
from . import api

urlpatterns = [
    path('api/meals/', api.MealListview.as_view(), name='meal-search'),
]