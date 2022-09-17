from django import forms
from .models import ThingspeakStation

class CreateThingspeakStationForm(forms.ModelForm):
    class Meta:
        model = ThingspeakStation
        fields = ['json',]
