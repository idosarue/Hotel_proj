import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')
django.setup()

from users.models import Room, RoomPrice, RoomType, CustomerPrice

def create_room_price():
    for price in [300, 700, 1200]:
        RoomPrice.objects.create(price=price)
# create_room_price()

def create_room_type():
    for index,room_name in enumerate(['suite', 'single', 'double']):
        RoomType.objects.create(name=room_name, price_per_night_id=index + 1)
# create_room_type()

def create_rooms():
    for _ in range(4):
        for room_type in RoomType.objects.all():
            Room.objects.create(room_type=room_type)
# create_rooms()

# CustomerPrice.objects.create()