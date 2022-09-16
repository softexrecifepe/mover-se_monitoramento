from django.urls import path
from . import views

app_name = 'thingspeak'

urlpatterns = [
    path("station/new-station", views.newStationThingspeak, name='new_station_thinkspeak')
]
