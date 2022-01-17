from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    # path('rooms/<str:bookings>/<int:adults_count>/<int:children_count>/', views.RoomsResults.as_view(), name='rooms'),
    # path('rooms', views.RoomsResults.as_view(), name='rooms'),
    path('rooms', views.test, name='rooms'),
    path('next_room/<int:room_id>/<int:booking_id>/<int:last_booking>/<int:room_num>/<int:adults_count>/<int:children_count>/<int:length>/', views.next_room, name='next_room'),
    path('check_out', views.CheckOut.as_view(), name='check_out')
]
