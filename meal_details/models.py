from django.db import models

class MealDetail100g(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='meals')
    protein = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()
    calories = models.IntegerField()
    def __str__(self):
        return self.name