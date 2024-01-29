# Generated by Django 4.2.6 on 2023-12-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedseats',
            name='passenger_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookedseats',
            name='passenger_gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bookedseats',
            name='passenger_mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='bookedseats',
            name='passenger_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
