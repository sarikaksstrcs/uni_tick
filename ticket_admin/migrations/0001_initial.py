<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-03-19 01:27
=======
# Generated by Django 4.1.7 on 2023-03-19 00:44
>>>>>>> 63fe77f3e299a23b47ce021ea39001138e661739

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=150)),
                ('total_tickets', models.IntegerField()),
                ('parking_available', models.BooleanField(default=False)),
                ('parking_max_capacity', models.IntegerField(blank=True, null=True)),
                ('booking_open', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingTicketTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('2 Wheeler', '2 Wheeler'), ('4 Wheeler', '4 Wheeler')], max_length=150, unique=True)),
                ('capacity', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.event')),
            ],
        ),
        migrations.CreateModel(
            name='TouristSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('parking_available', models.BooleanField(default=False)),
                ('parking_max_capacity', models.IntegerField(blank=True, null=True)),
                ('booking_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('capacity', models.IntegerField(default=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.event')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$', 'Please enter a valid email')])),
                ('persons_count', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4)])),
                ('parking_needed', models.BooleanField(default=False)),
                ('is_inside', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.event')),
                ('parking_tier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.parkingtickettier')),
                ('tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.tickettier')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_type', models.CharField(choices=[('2 Wheeler', '2 Wheeler'), ('4 Wheeler', '4 Wheeler')], max_length=150)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.ticket')),
            ],
        ),
    ]
