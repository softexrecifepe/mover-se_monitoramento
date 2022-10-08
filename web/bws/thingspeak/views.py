from django.shortcuts import render
from django.contrib import messages
from station.models import Station
from thingspeak.models import ThingspeakStation
from thingspeak.thingspeker_parser import ThingspekerParser
from .forms import CreateThingspeakStationForm
from django.contrib.auth.decorators import login_required


def viewStationThingspeak(request):
    stations_thing = ThingspeakStation.objects.all()
    other_stations = Station.objects.exclude(station_type__key='thing_station')
    return render(request, 'thingspeak/view_thingspeak_station.html', {'stations_thingspeak': stations_thing, 'others_station': other_stations})

@login_required
def newStationThingspeak(request):
    
    if request.method == 'POST':
        form = CreateThingspeakStationForm(request.POST)

        if form.is_valid():
            json = form.cleaned_data['json']
            #create_station_from_json()
            thingspeak_station_model = form.save(commit=False)
            tp = ThingspekerParser(json, thingspeak_station_model)
            tp.parse_station()
            
            if tp.is_valid(request):
                tp.create_models()
                messages.success(request, f'Estação {tp.thing_station_model.channel} cadastrada com sucesso!')
            else:
                messages.error(request, 'Os dados da estação não são válidos')
        else:
            messages.error(request, 'O formulário possui Informações inválidas')




    return render(request, 'thingspeak/create_thingspeak_station.html')#, {'alerts': alerts, 'stations': stations, 'time': time, 'operator': operator, 'form': form})
