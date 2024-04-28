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
    def __str__(self):
        return self.name
    