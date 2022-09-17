


from dataclasses import field
from station.models import Sensor, SensorStation, Station, StationType
from thingspeak.models import ThingspeakStation
from django.utils.dateparse import parse_datetime


class ThingspekerParser():
    FIELD_KEY = 'field'

    def __init__(self, json : dict, thing_station_model: ThingspeakStation):
        self.json = json
        self.thing_station_model = thing_station_model
        self.field_available = []

    def parse_create_station(self):
        
        if self.__is_channel():
            self.thing_station_model.channel = self.__get_in_channel('id')
            name = self.__get_in_channel('name')
            latitude = self.__get_in_channel('latitude')
            longitude = self.__get_in_channel('longitude')
            self.station_model, _ = Station.objects.get_or_create(
                                    identification = name, 
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
        else:
            pass # error
        

        self.validade_station()
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
        
    def validade_station(self):
        pass

    def __is_channel(self):
        return 'channel' in self.json

    def __get_in_channel(self, attr : str):
        value = None
        if attr in self.json['channel']:
            value = self.json['channel'][attr]
        return value