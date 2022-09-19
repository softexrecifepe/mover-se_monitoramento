from email.mime import base
from django.db import models
from station.models import Sensor, Station
from colorfield.fields import ColorField
from urllib import parse

# Create your models here.

class ThingspeakStation(models.Model):
    id  = models.AutoField(primary_key=True)
    json = models.JSONField()
    channel = models.CharField(max_length=20, unique=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.channel} - {self.station}"

class ThingspeakChartConfig(models.Model):
    CHART_URL="https://thingspeak.com/channels/%s/charts/%s"

    #http://thingspeak.umwelt-campus.de/docs/charts
    TYPES_CHOICES = (
                ('line', 'Line'), 
                ('spline', 'Spline'),
                ('bar', 'Bar'),
                ('column', 'Column'),
                ('spline', 'Spline')
            )
    
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]

    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    background_color = ColorField(default="#FFFFFF", samples=COLOR_PALETTE)
    chart_color = ColorField(default="#000000", samples=COLOR_PALETTE)
    days = models.IntegerField(default=30, blank=False)
    dynamic = models.BooleanField(default=True)
    sample = models.IntegerField(default=100, blank=False)
    type = models.CharField(max_length=50, choices=TYPES_CHOICES, default="spline")
    xaxis_text = models.CharField(max_length=50, blank=False, default="Hora")
    yaxis_text = models.CharField(max_length=50, blank=False)
    #width = models.CharField(max_length=10, default="auto")
    #height = models.CharField(max_length=10, default="auto")

    def get_request(self, channel, field):
        base_url = ThingspeakChartConfig.CHART_URL % (channel, field)
        dict_params={
            'bgcolor': self.background_color, 
            'color': self.chart_color, 
            'days': self.days, 
            'dynamic': self.dynamic, 
            'results': self.sample, 
            'title': self.title, 
            'type': self.type, 
            'xaxis': self.xaxis_text, 
            'yaxis': self.yaxis_text, 
            'width': 'auto',
            'height': 'auto'
        }
        params = parse.urlencode(dict_params)

        url = f'{base_url}?{params}'

        return url

    def __str__(self):
        return f"{self.id} - {self.title}"


class ChartConfigSensor(models.Model):
    config = models.ForeignKey(ThingspeakChartConfig, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.config} - {self.sensor}"