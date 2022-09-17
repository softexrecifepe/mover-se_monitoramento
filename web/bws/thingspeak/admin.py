from django.contrib import admin

from thingspeak.models import ThingspeakStation

# Register your models here.
@admin.register(ThingspeakStation)
class StationTypeAdmin(admin.ModelAdmin):
    list_display = ('channel', 'station',)
    fields = ('channel', 'station',)