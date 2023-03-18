from django.forms import ModelForm
from ticket_admin.models import Ticket
from django import forms

PARKING_CHOICES = (
    ('2 Wheeler', '2 Wheeler'),
    ('4 Wheeler', '4 Wheeler'),
)

class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [       
        'tier', 
        'name', 
        'email', 
        'persons_count', 
        'parking_needed',
        'parking_tier'
    ]

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)



