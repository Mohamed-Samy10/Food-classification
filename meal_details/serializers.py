from rest_framework import serializers
from .models import MealDetail100g

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealDetail100g
        fields = ['name','image','protein','fats','carbs','calories']