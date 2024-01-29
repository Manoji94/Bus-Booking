from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BusRoutes
from .serializer import BusrouteSerializer

class BusRouteView(APIView):
    def get(self, request, *args, **kwargs):
        rows = BusRoutes.objects.all()
        srows = BusrouteSerializer(rows, many=True)
        return Response({'rows': srows.data})
