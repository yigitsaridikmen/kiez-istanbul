from django import forms
from .models import PlaceInfo

class PlaceForm(forms.ModelForm):
    class Meta:
        model = PlaceInfo
        fields = [
     #  'user',    
    'name',
    'address',
    'county',
    'district',
    'place_type',
    'largegroup',
    'alone',
    'dateable',
    'price_category',
    'kitchen',
    'smoke',
    'door_policy',
    'readable',
    'workable',
    'loudness',
    'comment' 
        ]
    widgets = {
    'user': forms.HiddenInput(),  # Use HiddenInput widget for the 'user' field
    }