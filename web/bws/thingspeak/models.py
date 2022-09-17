from django.db import models
from station.models import Station
# Create your models here.

class ThingspeakStation(models.Model):
    id  = models.AutoField(primary_key=True)
    json = models.JSONField()
    channel = models.CharField(max_length=20, unique=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
