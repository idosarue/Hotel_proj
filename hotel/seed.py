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





def  create_booking():
    # Booking.objects.create(check_in_date=date(2022, 11, 1), check_out_date=date(2022, 11, 12))
    # booking = Booking.objects.first()
    # booking.room.add(Room.objects.all()[1])
    # # print(Room.objects.first().booking)
    # print(Room.objects.all()[1].booking_set.all())
    print(Booking.objects.all())
    
# create_booking()

def display_rooms():
    li = []
    check_in_date = datetime.strptime('1/7/2022', '%m/%d/%Y').date()
    check_out_date = datetime.strptime('1/8/2022', '%m/%d/%Y').date()

    li.append([room for room in Room.objects.all()[:10] if room.is_vacant(check_in_date, check_out_date)]) 

    return li


print(display_rooms())