from django.shortcuts import render, redirect
from .models import Event, TicketTier, ParkingTicketTier,TouristSpot
from .forms import CreateEventForm, CreateTicketTierForm,CreateParkingTierForm,CreateTourismForm


def index(request):
    return render(request, 'ticket_admin/index.html')

def events(request):
    events = Event.objects.all()
    return render(request, 'ticket_admin/events.html', context={'events': events})


def event_details(request, id):
    event = Event.objects.get(id=id)
    ticket_tiers = TicketTier.objects.filter(event=event)
    parking_tiers = ParkingTicketTier.objects.filter(event=event)
    return render(request, 'ticket_admin/event_details.html', context={'event': event, 'ticket_tiers': ticket_tiers, 'parking_tiers': parking_tiers})


def create_event(request):
    form = CreateEventForm()
    if request.POST:
        form = CreateEventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ticket_admin:events')
    return render(request, 'ticket_admin/create_event.html', context={'form': form})


def update_event(request, id):
    event = Event.objects.get(id=id)
    form = CreateEventForm(instance=event)
    if request.POST:
        form = CreateEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('ticket_admin:events')
    return render(request, 'ticket_admin/create_event.html', context={'form': form})


def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('ticket_admin:events')


def create_ticket_tier(request, id):
    event = Event.objects.get(id=id)
    form = CreateTicketTierForm()
    if request.POST:
        form = CreateTicketTierForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            form.save()
            return redirect('ticket_admin:event_details', id=id)
    return render(request, 'ticket_admin/create_ticket_tier.html', context={'form': form, 'event': event})

def update_ticket_tier(request, id):
    ticket_tier = TicketTier.objects.get(id=id)
    form = CreateTicketTierForm(instance=ticket_tier)
    if request.POST:
        form = CreateTicketTierForm(request.POST, instance=ticket_tier)
        if form.is_valid():
            form.save()
            return redirect('ticket_admin:event_details', id=id)
    return render(request, 'ticket_admin/create_event.html', context={'form': form})

def delete_ticket_tier(request, id):
    ticket_tier = TicketTier.objects.get(id=id)
    ticket_tier.delete()
    return redirect('ticket_admin:event_details', id=id)

#####################################################################################
# TOURIST SPOTS
#####################################################################################
def tourist_spots(request):
    tourist_spots= TouristSpot.objects.all()
    return render(request, 'ticket_admin/tourist_spots.html', context={'tourist_spots': tourist_spots,})

def tourist_spots_details(request, id):
    tourist_spots = TouristSpot.objects.get(id=id)
    ticket_tiers = TicketTier.objects.filter(event=tourist_spots)
    parking_tiers = ParkingTicketTier.objects.filter(event=tourist_spots)
    return render(request, 'ticket_admin/tourist_spots_details.html', context={'tourist_spots': tourist_spots,'ticket_tiers': ticket_tiers, 'parking_tiers': parking_tiers})


def create_tourist_spots(request):
    form = CreateTourismForm()
    if request.POST:
        form = CreateTourismForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_admin:tourist_spots')
    return render(request, 'ticket_admin/create_tourist_spots.html', context={'form': form})

#####################################################################################
# PARKING
#####################################################################################


def create_parking_tier(request, id):
    event = Event.objects.get(id=id)
    form = CreateParkingTierForm()
    if request.POST:
        form = CreateParkingTierForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event = event
            form.save()
            return redirect('ticket_admin:event_details', id=id)
    return render(request, 'ticket_admin/create_ticket_tier.html', context={'form': form, 'event': event})


