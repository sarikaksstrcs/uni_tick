from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
import qrcode


PARKING_CHOICES = (
    ('2 Wheeler', '2 Wheeler'),
    ('4 Wheeler', '4 Wheeler'),
)

AMNETIES_CHOICES = (
    ('rest room','rest room'),
    ('feeding room','feeding room'),
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
    image = models.ImageField(null=True,blank=True, upload_to="images/")

    

class TouristSpot(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
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
    #qr_code = models.ImageField(upload_to="qr_codes",null=True,blank=True)

    def save(self,*args,**kwargs):
        qrcode_img = qrcode.make(self.email)
        canvas = Image.new('RGB',(360,360),'white')
        draw = ImageDraw.Draw(canvas)

        canvas.paste(qrcode_img)

        fname = f'qr_code-{self.email}'+'.png'
        buffer = BytesIO()

        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()

        super().save(*args,**kwargs)


class ParkingTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    parking_type = models.CharField(max_length=150, choices=PARKING_CHOICES)


class ParkingTicketTier(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, choices=PARKING_CHOICES, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.capacity} slots remaining)'
    

########################################################
# AMENITIES
####################################################

"""class Amenities(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location =models.CharField(max_length=150)
    type = models.CharField(max_length=150, choices=AMNETIES_CHOICES)
    """

