# Generated by Django 3.2.18 on 2023-03-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_admin', '0004_amenity'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]