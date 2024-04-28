from rest_framework import generics, status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import DietPlan
from accounts.models import CustomUser
from .serializers import DietPlanSerializer

class DietPlanAPIView(generics.ListAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def suggest_diet_plan(request):
    user_id = request.user.id
    user = CustomUser.objects.get(pk=user_id)
    ideal_weight = user.height - 100
    weight_difference = user.weight - ideal_weight

    try:
        if weight_difference > 30:
            suggested_plan = DietPlan.objects.get(name="easy")
        elif weight_difference > 20:
            suggested_plan = DietPlan.objects.get(name="medium")
        elif weight_difference > 10:
            suggested_plan = DietPlan.objects.get(name="hard")
        elif weight_difference > 0:
            suggested_plan = DietPlan.objects.get(name="extreme")
        elif weight_difference == 0:
            return Response({"message": "Congratulations! You are at your ideal weight."})
        elif weight_difference < -20:
            suggested_plan = DietPlan.objects.get(name="easy-slim")
        elif weight_difference < -10:
            suggested_plan = DietPlan.objects.get(name="medium-slim")
        elif weight_difference < 0:
            suggested_plan = DietPlan.objects.get(name="hard-slim")
        else:
            return Response({"message": "Diet plan not available"}, status=status.HTTP_404_NOT_FOUND)
    except DietPlan.DoesNotExist:
        return Response({"message": "Diet plan not available"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DietPlanSerializer(suggested_plan)
    return Response(serializer.data)
