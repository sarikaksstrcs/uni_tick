from django.forms import ModelForm
from .models import Event, TicketTier, ParkingTicket, ParkingTicketTier, TouristSpot, Amenity
from django import forms


class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class CreateTicketTierForm(ModelForm):
    class Meta:
        model = TicketTier
        fields = [
            'title',
            'price',
            'capacity'
        ]


class CreateParkingTierForm(ModelForm):
    class Meta:
        model = ParkingTicketTier
        fields = [
            'title',
            'capacity'
        ]


class CreateTourismForm(ModelForm):
    class Meta:
        model = TouristSpot
        fields = '__all__'


class CreateAmenityForm(ModelForm):
    class Meta:
        model = Amenity
        fields = ['type', 'location', 'description']
