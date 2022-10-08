from dataclasses import field
from station.models import Sensor, SensorStation, Station, StationType
from thingspeak.models import ThingspeakStation
from django.utils.dateparse import parse_datetime
from django.contrib import messages


class ThingspekerParser():
    FIELD_KEY = 'field'

    def __init__(self, json : dict, thing_station_model: ThingspeakStation):
        self.json = json
        self.thing_station_model = thing_station_model
        self.field_available = []

    def parse_station(self):
        
        if self.__is_channel():
            self.thing_station_model.channel = self.__get_in_channel('id')
            name = self.__get_in_channel('name')
            latitude = self.__get_in_channel('latitude')
            longitude = self.__get_in_channel('longitude')
            self.station_model, _ = Station.objects.get_or_create(
                                    name = name,
                                    identification = name.lower().replace(' ', '_'), 
                                    latitude=latitude, 
                                    longitude=longitude)

            datetime_str = self.__get_in_channel('created_at')
            self.station_model.datetime_creation = parse_datetime(datetime_str)
            station_type, _ = StationType.objects.get_or_create(
                                    name='Thingspeak Station',
                                    key='thing_station',
                                )
            self.station_model.station_type = station_type
            self.thing_station_model.station = self.station_model
        
    def is_valid(self, request):
        is_valid = True
        if not self.__is_channel():
            is_valid = False
            messages.error(request, "\'Channel\' não está no JSON.")
        
        if not self.__is_station_valid():
            is_valid = False
            messages.error(request, 'Estação inválida')


        
        return is_valid
    
    def create_models(self):
        self.station_model.station_type.save()
        self.station_model.save()
        self.thing_station_model.save()
        self.find_fields()
        self.configure_fields()
    
    def configure_fields(self):
        for key, name in self.field_available:
            sensor, _ = Sensor.objects.get_or_create(
                key=key,
                name=name
            )
            sensor.save()

            sensorStation, _ = SensorStation.objects.get_or_create(
                station = self.station_model,
                sensor_type = sensor
            )
            sensorStation.save()

    def find_fields(self):
        for number in range(1, 30):
            curr_key = ThingspekerParser.FIELD_KEY+str(number)
            if (name := self.__get_in_channel(curr_key)):
                self.field_available.append((curr_key, name))
            else:
                break
        
    def __is_station_valid(self):
        return True

    def __is_channel(self):
        return 'channel' in self.json

    def __get_in_channel(self, attr : str):
        value = None
        if attr in self.json['channel']:
            value = self.json['channel'][attr]
        return value