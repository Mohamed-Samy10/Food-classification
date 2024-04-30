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
    
    if weight_difference == 0:
            return Response({"message": "Congratulations! You are at your ideal weight."})
    try:
        suggested_plan = DietPlan.objects.get(minimum_difference_weight__lte=weight_difference,maximum_difference_weight__gte=weight_difference)
    except DietPlan.DoesNotExist:
        return Response({"message": "Diet plan not available"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DietPlanSerializer(suggested_plan)
    return Response(serializer.data)
