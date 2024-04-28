# Generated by Django 4.2.7 on 2024-04-27 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_systems', '0002_day_rename_system_food_mealtype_dietplan_day_meal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='meal',
            new_name='meals',
        ),
        migrations.RenameField(
            model_name='dietplan',
            old_name='day',
            new_name='days',
        ),
        migrations.RenameField(
            model_name='mealtype',
            old_name='food',
            new_name='foods',
        ),
    ]
