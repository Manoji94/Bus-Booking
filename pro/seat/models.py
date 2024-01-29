from django.db import models

class BookedSeats(models.Model):
    no = models.AutoField(primary_key=True)
    sl_no = models.CharField(max_length=10)
    from_location = models.CharField(max_length=100, null=True, blank=True)
    to_location = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    departure_timings = models.CharField(max_length=50)
    selected_seats = models.CharField(max_length=250)
    passenger_name = models.CharField(max_length=100, null=True, blank=True)
    passenger_age = models.IntegerField(null=True, blank=True)
    passenger_gender = models.CharField(max_length=10, null=True, blank=True)
    passenger_mobile_number = models.CharField(max_length=15, null=True, blank=True)
    ticket_number = models.CharField(max_length=20, null=True, blank=True)
    ticket_price = models.FloatField(null=True, blank=True)
