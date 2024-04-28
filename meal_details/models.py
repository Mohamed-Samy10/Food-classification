from django.db import models

class MealDetail100g(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='meals')
    protein = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()
    calories = models.FloatField()
    def __str__(self):
        return self.name