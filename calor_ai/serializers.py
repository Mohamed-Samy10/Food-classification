from rest_framework import serializers
from .models import AnalyzedFood

class AnalyzedFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyzedFood
        fields = ['id', 'name', 'calories', 'carbs', 'fat', 'protein', 'volume', 'weight']
        
