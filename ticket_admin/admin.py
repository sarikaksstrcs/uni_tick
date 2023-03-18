from django.contrib import admin
from .models import Event, TicketTier, Ticket, ParkingTicket,TouristSpot
# Register your models here.

admin.site.register(Event)
admin.site.register(TicketTier)
admin.site.register(Ticket)
admin.site.register(ParkingTicket)
admin.site.register(TouristSpot)