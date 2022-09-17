from django.shortcuts import render
from django.contrib import messages
from station.models import Station
from thingspeak.models import ThingspeakStation
from thingspeak.thingspeker_parser import ThingspekerParser
from .forms import CreateThingspeakStationForm
from django.contrib.auth.decorators import login_required


def viewStationThingspeak(request):
    stations_thing = ThingspeakStation.objects.all()
    return render(request, 'thingspeak/view_thingspeak_station.html', {'stations': stations_thing})

@login_required
def newStationThingspeak(request):
    
    if request.method == 'POST':
        form = CreateThingspeakStationForm(request.POST)

        if form.is_valid():
            json = form.cleaned_data['json']
            #create_station_from_json()
            thingspeak_station_model = form.save(commit=False)
            tp = ThingspekerParser(json, thingspeak_station_model)
            tp.parse_create_station()            
            messages.success(request, 'Estação cadastrada com sucesso!')




    return render(request, 'thingspeak/create_thingspeak_station.html')#, {'alerts': alerts, 'stations': stations, 'time': time, 'operator': operator, 'form': form})
