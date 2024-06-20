from datetime import datetime, timedelta
import requests
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import AnalyzedFood
from .serializers import AnalyzedFoodSerializer
from accounts.models import CustomUser

FLASK_API_URL = 'http://34.197.217.211:8000/upload'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_and_analyze(request):
    user = request.user
    try:
        if 'image' not in request.data:
            return Response({'error': 'Image file not found in request'}, status=status.HTTP_400_BAD_REQUEST)
        
        image_file = request.data['image']
        files = {'image': image_file}
        
        response = requests.post(FLASK_API_URL, files=files)
        
        if response.status_code == 200:
            data = response.json()
            
            foods = []

            for key, food_data in data.items():
                if key.startswith('object_'):
                    nutrition_content = food_data.get('Nutrition Content', {})
                    
                    food = AnalyzedFood(
                        user=user,  
                        name=food_data.get('Name', ''),
                        calories=food_data.get('Calories', 0.0),
                        carbs=nutrition_content.get('Carbs', 0.0),
                        fat=nutrition_content.get('Fat', 0.0),
                        protein=nutrition_content.get('Protein', 0.0),
                        volume=food_data.get('Volume', 0.0),
                        weight=food_data.get('Weight', 0.0)
                    )
                    food.save()
                    foods.append(food)
            
            path = data.get('path', '')  
            serializer = AnalyzedFoodSerializer(foods, many=True)
            
            response_data = {
                'path': path,
                'foods': serializer.data
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        else:
            error_msg = f'Failed to analyze image. {response.status_code}.'
            return Response({'error': error_msg}, status=response.status_code)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def daily_report(request):
    today = datetime.now().date()
    foods_today = AnalyzedFood.objects.filter(user=request.user, analyzed_at__date=today)
    report_data = calculate_report(foods_today)
    return Response(report_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def weekly_report(request):
    try:
        today = datetime.now().date()
        week_ago = today - timedelta(days=7)
        
        report_data = []
        current_date = week_ago
        while current_date <= today:
            foods_for_day = AnalyzedFood.objects.filter(user=request.user, analyzed_at__date=current_date)
            
            daily_data = calculate_report(foods_for_day)
            
            daily_data['date'] = current_date.strftime('%Y-%m-%d')
            
            report_data.append(daily_data)
            
            current_date += timedelta(days=1)
        
        return Response(report_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def calculate_report(foods):
    total_calories = sum(food.calories for food in foods)
    total_carbs = sum(food.carbs for food in foods)
    total_fat = sum(food.fat for food in foods)
    total_protein = sum(food.protein for food in foods)
    
    report_data = {
        'total_calories': total_calories,
        'total_carbs': total_carbs,
        'total_fat': total_fat,
        'total_protein': total_protein
    }
    return report_data