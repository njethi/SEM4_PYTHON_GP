from django.db import models

# Create your models here.
class Weather(models.Model):
    country = models.CharField(max_length=100)
    temprature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    precipitation = models.FloatField()
