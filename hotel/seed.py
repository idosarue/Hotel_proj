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
    for num in range(3):
        # Loop through the ziped lists, None for a single room that doesnt have children
        for price, room_type, max_adults, max_children in list(zip(prices, room_types, [1,2,3], [0,2,2])):
            Room.objects.create(number_of_adult_beds = max_adults, number_of_children_beds = max_children, room_price = price, room_type = room_type, max_adults=max_adults, max_children=max_children)
# create_rooms()




# ************* tests***********

get_request = {'room-1-children': "0", 'room-1-adults': '1', 'room-2-children': '0', 'room-2-adults': "1", 'check_in_date': '2021-12-01', 'check_out_date': '2021-12-22'}

def validate_dates(get_request):
    try:
        check_in_date = datetime.strptime(get_request['check_in_date'], '%Y-%m-%d').date()
        check_out_date = datetime.strptime(get_request['check_out_date'], '%Y-%m-%d').date()
    except (ValueError, KeyError):
        check_in_date = date.today()
        check_out_date = check_in_date + dt.timedelta(days=1)
    if check_in_date < check_out_date: return {'check_in_date' : check_in_date, 'check_out_date' : check_out_date}
    return {'check_in_date' : check_in_date, 'check_out_date' : check_in_date + dt.timedelta(days=1)}


def validate_guests(get_request, room_count):
    try:
        rooms2 = [
        RoomType.objects.filter(room__max_children__gte=int(get_request[f'room-{num + 1}-children']),
        room__max_adults__gte = int(get_request[f'room-{num + 1}-adults'])).distinct()
        for num in range(room_count)]
    except KeyError:
        return 'an error occurd'

    return rooms2


def display_rooms(rooms):
    li = []
    check_in_date = validate_dates(get_request)['check_in_date']
    check_out_date = validate_dates(get_request)['check_out_date']
    print(check_in_date)
    try:
        for index, obj in enumerate(rooms):
            li.append(list(room.room_set.all()[index] for room in obj))
    except IndexError:
        return 'no available rooms'

    for obj in li:
        for room in obj:
            if room.is_vacant('2021-12-13', '2021-12-14'):
                continue
            print('no')
            return

    return li


