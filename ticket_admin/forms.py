from django.forms import ModelForm
from .models import Event, TicketTier,ParkingTicket,ParkingTicketTier
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

