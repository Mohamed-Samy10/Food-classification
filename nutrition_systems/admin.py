from django.contrib import admin
from .models import Food, MealType, Day, DietPlan

admin.site.register(Food)
admin.site.register(MealType)
admin.site.register(Day)
admin.site.register(DietPlan)
