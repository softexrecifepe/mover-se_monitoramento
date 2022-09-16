from django import forms
from .models import ThinkspeakStation

class CreateThingspeakStationForm(forms.ModelForm):
    class Meta:
        model = ThinkspeakStation
        fields = ['json',]
