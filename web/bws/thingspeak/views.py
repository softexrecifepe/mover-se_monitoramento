from django.shortcuts import render
from .forms import CreateThingspeakStationForm

@login_required
def newStationThingspeak(request):
    
    if request.method == 'POST':
        form = CreateThingspeakStationForm(request.POST)
        print(form)

        if form.is_valid():
            pass


    return render(request, 'thingspeak/create_thingspeak_station.html')#, {'alerts': alerts, 'stations': stations, 'time': time, 'operator': operator, 'form': form})
