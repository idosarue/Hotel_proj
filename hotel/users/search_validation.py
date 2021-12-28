from datetime import datetime,date
import datetime as dt
from django.contrib import messages
from .models import Room, RoomType


def validate_dates(get_request):
    try:
        check_in_date = datetime.strptime(get_request['check_in_date'], '%Y-%m-%d').date()
        check_out_date = datetime.strptime(get_request['check_out_date'], '%Y-%m-%d').date()
    except (ValueError, KeyError):
        check_in_date = date.today()
        check_out_date = check_in_date + dt.timedelta(days=1)
    if check_in_date < check_out_date: return {'check_in_date' : check_in_date, 'check_out_date' : check_out_date}
    return {'check_in_date' : check_in_date, 'check_out_date' : check_in_date + dt.timedelta(days=1)}


def validate_guests(request, room_count):
    get_request = request.GET
    try:
        rooms2 = [
        RoomType.objects.filter(room__max_children__gte=int(get_request[f'room-{num + 1}-children']),
        room__max_adults__gte = int(get_request[f'room-{num + 1}-adults'])).distinct()
        for num in range(room_count)]
    except KeyError:
        return messages.error(request, 'an error occurd')

    return display_rooms(request, rooms2)


def display_rooms(request,rooms):
    li = []
    get_request = request.GET
    check_in_date = validate_dates(get_request)['check_in_date']
    check_out_date = validate_dates(get_request)['check_out_date']
    try:
        for index, obj in enumerate(rooms):
            li.append(list(room.room_set.all()[index] for room in obj))
    except IndexError:
        return messages.error(request, 'no available rooms')

    for obj in li:
        for room in obj:
            if room.is_vacant(check_in_date, check_out_date):
                continue
            return messages.error(request, 'no available rooms')

    return li