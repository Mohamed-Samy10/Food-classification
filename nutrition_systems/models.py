from django.db import models


class Food(models.Model) :
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
            
class MealType(models.Model):
    name = models.CharField(max_length=50)
    foods = models.ManyToManyField(Food)
    def __str__(self):
        return self.name
    
class Day(models.Model):
    name = models.CharField(max_length=50)
    meals = models.ManyToManyField(MealType)
    def __str__(self):
        return self.name
    
class DietPlan(models.Model) :
    name = models.CharField(max_length=50)
    days = models.ManyToManyField(Day)
    minimum_difference_weight = models.PositiveSmallIntegerField()
    maximum_difference_weight = models.SmallIntegerField()
    def __str__(self):
        return f"{self.name}: from {self.minimum_difference_weight} to {self.maximum_difference_weight}"
    