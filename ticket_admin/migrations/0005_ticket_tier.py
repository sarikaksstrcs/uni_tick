# Generated by Django 4.1.7 on 2023-03-17 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_admin', '0004_alter_tickettier_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ticket_admin.tickettier'),
            preserve_default=False,
        ),
    ]
