import os
import django
from django.forms.formsets import all_valid
from datetime import datetime, date
import datetime as dt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')
django.setup()

from users.models import Booking, Room, RoomPrice,CustomerPrice, RoomType

# Create room prices
def create_room_price():
    for price in [300, 700, 1200]:
        RoomPrice.objects.create(price=price)
# create_room_price()

# Create room Types
def create_room_types():
    images = ['single_room.png', 'double_room.png', 'suite.png']
    for index, room_type in enumerate(['Single', 'Double', 'Suite']):
        RoomType.objects.create(name=room_type, image=images[index])
# create_room_types()

# Create Rooms with the 3 types of prices, types(Single, Double, Suite)
def create_rooms():
    prices = RoomPrice.objects.all()
    room_types = RoomType.objects.all()
    for num in range(9):
        # Loop through the ziped lists, None for a single room that doesnt have children
        for price, room_type, max_adults, max_children in list(zip(prices, room_types, [1,2,3], [0,2,2])):
            Room.objects.create(number_of_adult_beds = max_adults, number_of_children_beds = max_children, room_price = price, room_type = room_type, max_adults=max_adults, max_children=max_children)
# create_rooms()




# ************* tests***********

check_in_date = datetime.strptime('1/7/2022', '%m/%d/%Y').date()
check_out_date = datetime.strptime('1/8/2022', '%m/%d/%Y').date()


def  create_booking():
    Booking.objects.create(check_in_date=check_in_date, check_out_date=check_out_date)
    Booking.objects.first().rooms.add(Room.objects.first(), Room.objects.all()[1])
# create_booking()


request = {'room-1-children' : '0', 'room-1-adults': '1', 'room-2-children' : '0', 'room-2-adults': '3'}

def check_vacant(room_type):
    for room in room_type.room_set.all():
        if room.is_vacant(check_in_date, check_out_date):
            return room


def validate_guests(request, room_count):
    try:
        rooms2 = [
        RoomType.objects.filter(room__max_children__gte=[int(request[f'room-{num + 1}-children']) if request[f'room-{num + 1}-children'].isnumeric() and 0 < int(request[f'room-{num + 1}-children']) < 3  else 0][0],
        room__max_adults__gte =[int(request[f'room-{num + 1}-adults']) if request[f'room-{num + 1}-adults'].isnumeric() and 1 < int(request[f'room-{num + 1}-adults']) < 4  else 1][0]).distinct()
        for num in range(room_count)]

        # rooms2 = [
        # Room.objects.filter(max_children__gte=[int(request[f'room-{num + 1}-children']) if request[f'room-{num + 1}-children'].isnumeric() and 0 < int(request[f'room-{num + 1}-children']) < 3  else 0][0],
        # max_adults__gte =[int(request[f'room-{num + 1}-adults']) if request[f'room-{num + 1}-adults'].isnumeric() and 1 < int(request[f'room-{num + 1}-adults']) < 4  else 1][0]).distinct()
        # for num in range(room_count)]

    except KeyError:
        print('error')
        return 

    

    check_in_date = datetime.strptime('1/7/2022', '%m/%d/%Y').date()
    check_out_date = datetime.strptime('1/8/2022', '%m/%d/%Y').date()
    bookings = [Booking.objects.create(check_in_date=check_in_date, check_out_date=check_out_date) for num in range(room_count)]

    li = []
    available_rooms = []
    for num in range(room_count):
        for obj in rooms2[num]:
            bookings[num].rooms.add(check_vacant(obj))

    
    for booking in bookings:
        print(booking.rooms.all())

    return rooms2

# validate_guests(request, 2)


def display_rooms():
    li = []
    check_in_date = datetime.strptime('1/7/2022', '%m/%d/%Y').date()
    check_out_date = datetime.strptime('1/8/2022', '%m/%d/%Y').date()

    li.append([room for room in Room.objects.all()[:10] if room.is_vacant(check_in_date, check_out_date)]) 

    return li


# print(display_rooms())


def delete_bookings():
    for booking in Booking.objects.all():
        booking.delete()

# delete_bookings()


print(sorted(Booking.objects.get(id=240).rooms.all(), key=lambda x: x.room_price.price))