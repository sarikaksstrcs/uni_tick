from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator

PARKING_CHOICES = (
    ('2 Wheeler', '2 Wheeler'),
    ('4 Wheeler', '4 Wheeler'),
)


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=150)
    total_tickets = models.IntegerField()
    parking_available = models.BooleanField(default=False)
    parking_max_capacity = models.IntegerField(null=True, blank=True)
    booking_open = models.BooleanField(default=True)


class TicketTier(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    capacity = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.title}: ₹{self.price} ({self.capacity} seats remaining)'

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tier = models.ForeignKey(TicketTier,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, validators=[RegexValidator(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", 'Please enter a valid email')])
    persons_count = models.IntegerField(default=1, validators=[MaxValueValidator(4)])
    parking_needed = models.BooleanField(default=False)
    parking_tier = models.ForeignKey('ParkingTicketTier', on_delete=models.CASCADE, null=True, blank=True)
    is_inside = models.BooleanField(default=False)
    


class ParkingTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    parking_type = models.CharField(max_length=150, choices=PARKING_CHOICES)


class ParkingTicketTier(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, choices=PARKING_CHOICES, unique=True)
    location = models.CharField(max_length=100,null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.capacity} slots remaining)'