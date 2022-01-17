from django.contrib.auth.models import GroupManager
from django.contrib.messages.api import success
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, FormView, DetailView, View
from django.views.generic.edit import CreateView
from .forms import RoomsDateForm, GuestsFormSet, someForm
from .models import Room
from django.contrib import messages
from django.http import JsonResponse, request
from .search_validation import create_booking
from django.core.paginator import Paginator
from urllib.parse import urlencode
from .models import Booking
from datetime import date, datetime
from django.urls import reverse_lazy
import re

class Home(FormView):
    template_name = 'users/home.html'
    form_class = RoomsDateForm

    def form_invalid(self, form):
        return JsonResponse({"error": form.errors}, status=400)
    

    def get_success_url(self):
        created_bookings = create_booking(self.request, int(f"{self.request.POST}".count("room")) // 2)
        return reverse_lazy('rooms', kwargs = {'bookings': f'{created_bookings[0]}', 'adults_count' : created_bookings[1], 'children_count' : created_bookings[2]})


class RoomsResults(CreateView):
    template_name = 'users/rooms.html'
    form_class = someForm

    # def get_booking(self):
    #     print(self.request.POST)
    #     bookings_li = self.kwargs['bookings'].replace('[', '').replace(']', '').split(',')
    #     try:
    #         return [Booking.objects.get(id=int(booking)) for booking in bookings_li]
    #     except ValueError:
    #         return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_booking():
            return messages.error(self.request, 'no avilable rooms')
        context['rooms'] = sorted(self.get_booking()[0].rooms.all(), key=lambda x: x.room_price.price)
        context['amount_of_rooms'] = len(self.get_booking()[0].rooms.all())
        context['booking'] = self.get_booking()[0]
        context['request'] = self.request.GET
        context['check_in_date'] = self.get_booking()[0].check_in_date
        context['check_out_date'] = self.get_booking()[0].check_out_date
        context['nights'] =  self.get_booking()[0].check_out_date.day - self.get_booking()[0].check_in_date.day
        context['last_booking'] = Booking.objects.last().id
        context['length'] = len(self.get_booking())
        context['adults_count'] = self.kwargs['adults_count']
        context['children_count'] = self.kwargs['children_count']
        context['room_count'] = [index + 1 for index, num in enumerate(self.get_booking())]
        context['room_num'] = 1
        return context

def test(request):
    post_request = request.POST
    created_bookings = create_booking(request, int(f"{post_request}".count("room")) // 2)
    first_booking = created_bookings['bookings'][0]
    context = dict()
    context['rooms'] = sorted(first_booking.rooms.all(), key=lambda x: x.room_price.price)
    context['amount_of_rooms'] = len(first_booking.rooms.all())
    context['bookings'] = created_bookings['bookings']
    context['request'] = request.GET
    context['check_in_date'] = first_booking.check_in_date
    context['check_out_date'] = first_booking.check_out_date
    context['nights'] =  first_booking.check_out_date.day - first_booking.check_in_date.day
    context['last_booking'] = Booking.objects.last().id
    context['length'] = len(created_bookings['bookings'])
    context['room_count'] = list(range(1, context['length'] + 1))
    context['room_num'] = 1
    context['adults_count'] = created_bookings['adults']
    context['children_count'] = created_bookings['children']
    context['booking'] = first_booking
    return render(request, 'users/rooms.html', context)

def next_room(request, room_id, booking_id, last_booking, room_num, adults_count, children_count, length):
    booking = get_object_or_404(Booking, id=booking_id)
    room = get_object_or_404(Room, id=room_id)
    rooms_to_remove = booking.rooms.exclude(id=room.id)
    print(last_booking-length, '89')
    for room_obj in rooms_to_remove:
        booking.rooms.remove(room_obj)
    booking.is_approved = True
    booking.total_price = room.room_price.price
    booking.save()
    if booking_id + 1 <= last_booking:
        booking = get_object_or_404(Booking, id=booking_id + 1)
        context = {
            'rooms': sorted(booking.rooms.all(), key=lambda x: x.room_price.price),
            'booking' : Booking.objects.get(id=booking_id + 1),
            'bookings' : [Booking.objects.get(id=num) for num in range(last_booking + 1 - length, last_booking + 1)],
            'last_booking' : last_booking, 
            'length' : length, 
            'room_num' : room_num + 1,
            'room_count' : list(range(1, length + 1)),
            'check_in_date' : booking.check_in_date,
            'check_out_date' : booking.check_out_date,
            'adults_count' : adults_count,
            'children_count' : children_count,
            'amount_of_rooms' : len(booking.rooms.all()),
            }
        context['total_for_stay'] = sum([booking.total_price for booking in context['bookings']])
        return render(request, 'users/rooms.html', context)
    else:
        last_booking += 1
        return render(request, 'users/check_out.html', {'bookings' : [Booking.objects.get(id=num) for num in range(last_booking - length, last_booking)]})


class CheckOut(ListView):
    template_name = 'users/check_out.html'
    model = Booking