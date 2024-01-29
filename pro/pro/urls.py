"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py
from django.contrib import admin
from django.urls import path, include
from app.views import BusRouteView
from seat.views import BookedSeatsView, ReserveSeatsView, SingleSeatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getroutes/', BusRouteView.as_view(), name='get_routes_api'),
    path('api/getseats/', BookedSeatsView.as_view(), name='get_seats_api'),
    path('api/reserveseats/', ReserveSeatsView.as_view(), name='reserve_seats_api'),
    path('api/getseat/<int:pk>/', SingleSeatView.as_view(), name='get_single_seat_api'),
    path('api/deleteseat/<int:pk>/', SingleSeatView.as_view(), name='delete_single_seat_api'),
]
