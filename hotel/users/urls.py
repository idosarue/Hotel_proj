from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('rooms/<str:bookings>/', views.RoomsResults.as_view(), name='rooms'),
    path('next_room/<int:room_id>/<int:booking_id>/<int:last_booking>/<int:length>/', views.next_room, name='next_room'),
    path('check_out', views.CheckOut.as_view(), name='check_out')
]
