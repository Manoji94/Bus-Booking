from rest_framework import serializers 
from . models import BusRoutes

class BusrouteSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = BusRoutes
		fields = '__all__'
