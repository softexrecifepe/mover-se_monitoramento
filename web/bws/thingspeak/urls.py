from django.urls import path
from . import views

app_name = 'thingspeak'

urlpatterns = [
    path("station/new-station", views.newStationThingspeak, name='new_station'),
    path("station/view-station", views.viewStationThingspeak, name='view_station')
]
