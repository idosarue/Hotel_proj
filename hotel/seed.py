import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')
django.setup()

from users.models import Room, RoomPrice,CustomerPrice, Suite, SingleRoom, DoubleRoom

def create_room_price():
    for price in [300, 700, 1200]:
        RoomPrice.objects.create(price=price)
# create_room_price()

def create_rooms():
    prices = RoomPrice.objects.all()
    for _ in range(3):
        SingleRoom.objects.create(number_of_adult_beds = 1, room_price = prices[0])
        DoubleRoom.objects.create(number_of_adult_beds = 2, room_price = prices[1])
        Suite.objects.create(number_of_adult_beds = 3, room_price = prices[2])
# create_rooms()


# CustomerPrice.objects.create()

def update_people_number_in_room(**kwargs):
    for room in kwargs['rooms']:
        room.max_adults = kwargs['number_of_adults']
        room.max_children = kwargs['number_of_children']
        room.number_of_children_beds = kwargs['number_of_children_beds']
        room.save()

update_people_number_in_room(number_of_adults = 2, number_of_children = 1, number_of_children_beds = 1, rooms = DoubleRoom.objects.all())

def print_room_data(rooms):
    for room in rooms:
        print(vars(room))

print_room_data(DoubleRoom.objects.all())

print(not [False, False])