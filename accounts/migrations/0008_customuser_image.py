# Generated by Django 4.2.7 on 2024-06-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='media/profile/anonymous.png', upload_to='media/profile'),
        ),
    ]
