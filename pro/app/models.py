from django.db import models

class BusRoutes(models.Model):
    sl_no = models.CharField(max_length=10, primary_key=True)
    depot = models.CharField(max_length=50)
    route_no = models.CharField(max_length=10)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    route_length = models.CharField(max_length=10)
    bus_type = models.CharField(max_length=50)
    no_of_service = models.CharField(max_length=50)
    departure_timings = models.CharField(max_length=50)