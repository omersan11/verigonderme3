from django.db import models

# Create your models here.
from django.db import models

from django.db import models

from django.db import models

from django.db import models

# Create your models here.
from django.db import models

class TextData(models.Model):
    text_input = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_input


class DistanceData(models.Model):
    distance = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.distance} cm at {self.timestamp}"


class TemperatureData(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.temperature} °C at {self.timestamp}"

class HumidityData(models.Model):
    humidity = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.humidity}% at {self.timestamp}"