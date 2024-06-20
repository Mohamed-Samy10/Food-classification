# calor_ai/models.py
from django.db import models
from accounts.models import CustomUser

class AnalyzedFood(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    volume = models.FloatField()
    weight = models.FloatField()
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"