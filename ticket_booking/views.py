from django.shortcuts import render, redirect
from ticket_admin.models import Event, TicketTier,ParkingTicketTier
from .forms import CreateTicketForm
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'ticket_booking/index.html')

def event(request):
    events = Event.objects.filter(booking_open =True)
    
    search_input = request.GET.get('search-area')
    if search_input:
        events = Event.objects.filter(Q(description__icontains=search_input))
        return render(request, 'ticket_booking/event.html', {'events': events})
    return render(request, 'ticket_booking/event.html',{'events':events})

def event_details(request, id):
    event = Event.objects.get(id=id)
    ticket_tiers = TicketTier.objects.filter(event=event, capacity__gt=0)
    parking_tiers = ParkingTicketTier.objects.filter(event=event)
    return render(request, 'ticket_booking/event_details.html', context={'event': event, 'ticket_tiers': ticket_tiers, 'parking_tiers': parking_tiers})


def book_ticket(request, id):
    event = Event.objects.get(id=id)
    form = CreateTicketForm()
    if request.POST:
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            tier = form.tier
            if tier.capacity < form.persons_count:
                form = CreateTicketForm(request.POST)
                form.add_error('tier', 'Sorry not enough tickets available for this tier')
                return render(request, 'ticket_booking/book_ticket.html', context={'form': form, 'event': event})
            tier.capacity -= form.persons_count
            """ if form.parking_needed:
                
                parking = ParkingTicket(ticket = form, type=form.parking_type)
                parking.save()"""
                
            tier.save()
            form.save()
            return redirect('ticket_booking:home')
    return render(request, 'ticket_booking/book_ticket.html', context={'form': form, 'event': event})
