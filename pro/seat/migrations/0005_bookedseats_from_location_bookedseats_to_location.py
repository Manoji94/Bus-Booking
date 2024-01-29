# Generated by Django 4.2.6 on 2023-12-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0004_bookedseats_ticket_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedseats',
            name='from_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookedseats',
            name='to_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
