from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin
from .models import TextData, DistanceData,TemperatureData , HumidityData

admin.site.register(TextData)
admin.site.register(DistanceData)
admin.site.register(TemperatureData)
admin.site.register(HumidityData)