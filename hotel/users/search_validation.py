from datetime import datetime,date
import datetime as dt
from django.contrib import messages
from django.db.models.query import QuerySet
from .models import Booking, Room, RoomType

def validate_dates(request):
    try:
        check_in_date = datetime.strptime(request['check_in_date'], '%m/%d/%Y').date()
        check_out_date = datetime.strptime(request['check_out_date'], '%m/%d/%Y').date()
    except (ValueError, KeyError):
        check_in_date = date.today()
        check_out_date = check_in_date + dt.timedelta(days=1)
    if date.today() < check_in_date and check_in_date <  check_out_date and check_out_date > date.today(): return {'check_in_date' : check_in_date, 'check_out_date' : check_out_date}
    return {'check_in_date' : date.today(), 'check_out_date' : date.today() + dt.timedelta(days=1)}


def validate_guests(request, room_count):
    try:
        rooms2 = [
        RoomType.objects.filter(room__max_children__gte=[int(request[f'room-{num + 1}-children']) if request[f'room-{num + 1}-children'].isnumeric() and 0 < int(request[f'room-{num + 1}-children']) < 3  else 0][0],
        room__max_adults__gte =[int(request[f'room-{num + 1}-adults']) if request[f'room-{num + 1}-adults'].isnumeric() and 1 < int(request[f'room-{num + 1}-adults']) < 4  else 1][0]).distinct()
        for num in range(room_count)]

    except KeyError:
        return messages.error(request, 'an error occurd')

    return display_rooms(request, rooms2)


def display_rooms(request,rooms):
    li = []
    check_in_date = validate_dates(request)['check_in_date']
    check_out_date = validate_dates(request)['check_out_date']

    try:
        for index, obj in enumerate(rooms):
            # the index is used to get the unique room object for every room type
            li.append([room.room_set.all()[index] for room in obj if room.room_set.all()[index].is_vacant(check_in_date, check_out_date)]) 
    except IndexError:
        return False
    return li


def create_booking(request, room_count):
    check_in_date = validate_dates(request.POST)['check_in_date']
    check_out_date = validate_dates(request.POST)['check_out_date']

    room_li = validate_guests(request.POST, room_count)
    if not room_li or not room_li[0]:
        return False
    bookings_li = [Booking.objects.create(check_in_date=check_in_date, check_out_date=check_out_date) for _ in range(room_count)]
        
    bookings_id_li = [booking.id for booking in bookings_li]

    for num in range(room_count):
        for room in room_li[num]:
            bookings_li[num].rooms.add(room)

    return bookings_id_li
