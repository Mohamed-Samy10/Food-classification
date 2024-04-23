from rest_framework import filters,generics
from .serializers import MealSerializer
from .models import MealDetail100g

class MealListview(generics.ListAPIView):
    queryset = MealDetail100g.objects.all()
    serializer_class = MealSerializer 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']