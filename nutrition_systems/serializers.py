from rest_framework import serializers
from .models import Food,MealType,Day,DietPlan

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name']
        
class MealTypeSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many='True')
    class Meta:
        model = MealType
        fields = ['name', 'foods']

class DaySerializer(serializers.ModelSerializer):
    meals = MealTypeSerializer(many='True')
    class Meta:
        model = Day
        fields = ['name', 'meals']

class DietPlanSerializer(serializers.ModelSerializer):
    days = DaySerializer(many='true')
    class Meta:
        model = DietPlan
        fields = ['name', 'days']