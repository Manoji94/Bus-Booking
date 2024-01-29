from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookedSeats
from .serializers import BookedSeatsSerializer

class BookedSeatsView(APIView):
    def get(self, request, *args, **kwargs):
        seats = BookedSeats.objects.all()
        serialized_seats = BookedSeatsSerializer(seats, many=True)
        return Response({'seats': serialized_seats.data})

class ReserveSeatsView(APIView):
    def post(self, request, *args, **kwargs):
        sl_no = request.data.get('sl_no')
        from_location = request.data.get('from_location')
        to_location = request.data.get('to_location')
        date = request.data.get('date')
        departure_timings = request.data.get('departure_timings')
        selected_seats = request.data.get('selected_seats')
        passenger_name = request.data.get('passenger_name')
        passenger_age = request.data.get('passenger_age')
        passenger_gender = request.data.get('passenger_gender')
        passenger_mobile_number = request.data.get('passenger_mobile_number')
        ticket_number = request.data.get('ticket_number')
        ticket_price = request.data.get('ticket_price')

        booked_seats = BookedSeats(
            sl_no=sl_no,
            from_location=from_location,
            to_location=to_location,
            date=date,
            departure_timings=departure_timings,
            selected_seats=selected_seats,
            passenger_name=passenger_name,
            passenger_age=passenger_age,
            passenger_gender=passenger_gender,
            passenger_mobile_number=passenger_mobile_number,
            ticket_number=ticket_number,
            ticket_price=ticket_price,
        )
        booked_seats.save()

        return Response({'message': 'Seats reserved successfully'}, status=status.HTTP_201_CREATED)

class SingleSeatView(APIView):
    def get(self, request, pk, *args, **kwargs):
        seat = BookedSeats.objects.get(pk=pk)
        serialized_seat = BookedSeatsSerializer(seat)
        return Response({'seat': serialized_seat.data})
        
    def delete(self, request, pk, *args, **kwargs):
        try:
            seat = BookedSeats.objects.get(ticket_number=pk)  # Use ticket_number instead of pk
            seat.delete()
            return Response({'message': 'Seat deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except BookedSeats.DoesNotExist:
            return Response({'error': 'Seat not found'}, status=status.HTTP_404_NOT_FOUND)

