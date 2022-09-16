from django.contrib import admin

from thingspeak.models import ThinkspeakStation

# Register your models here.
@admin.register(ThinkspeakStation)
class StationTypeAdmin(admin.ModelAdmin):
    list_display = ('channel', 'station',)
    fields = ('channel', 'station',)