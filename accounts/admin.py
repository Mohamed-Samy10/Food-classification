from django.contrib import admin
from .models import CustomUser,Profile

class ProfileAdmin (admin.ModelAdmin):
    readonly_fields =['id',]
admin.site.register(Profile,ProfileAdmin)
admin.site.register(CustomUser)
# Register your models here.
