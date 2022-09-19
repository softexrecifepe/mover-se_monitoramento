from django.contrib import admin

from thingspeak.models import ChartConfigSensor, ThingspeakChartConfig, ThingspeakStation

# Register your models here.
@admin.register(ThingspeakStation)
class StationTypeAdmin(admin.ModelAdmin):
    list_display = ('channel', 'station',)
    fields = ('channel', 'station',)

@admin.register(ThingspeakChartConfig)
class ThingspeakChartConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'background_color', 'chart_color', 'days', 'dynamic', 'sample', 'type', 'xaxis_text', 'yaxis_text')
    fields = ('title', 'background_color', 'chart_color', 'days', 'dynamic', 'sample', 'type', 'xaxis_text', 'yaxis_text')


@admin.register(ChartConfigSensor)
class ChartConfigSensorAdmin(admin.ModelAdmin):
    list_display = ('config', 'sensor')
    fields = ('config', 'sensor')