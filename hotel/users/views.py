from django.contrib.auth.models import GroupManager
from django.contrib.messages.api import success
from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from .forms import RoomsDateForm, GuestsFormSet
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
        print('invalid')
        return JsonResponse({"error": form.errors}, status=400)
    

    def get_success_url(self):
        return reverse_lazy('rooms', kwargs = {'bookings': f'{create_booking(self.request, int(f"{self.request.POST}".count("room")) // 2)}'})


class RoomsResults(ListView):
    template_name = 'users/rooms.html'
    model = Booking


    def get_booking(self):
        bookings_li = self.kwargs['bookings'].replace('[', '').replace(']', '').split(',')
        try:
            return [Booking.objects.get(id=int(booking)) for booking in bookings_li]
        except ValueError:
            return False

    def paginate_bookings(self):
        bookings = self.get_booking()
        paginator = Paginator(bookings, 1)
        page_num = self.request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        return page_obj 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_booking():
            return messages.error(self.request, 'no avilable rooms')

        context['booking'] = self.get_booking()[0]  
        context['request'] = self.request.GET
        context['check_in_date'] = self.get_booking()[0].check_in_date
        context['check_out_date'] = self.get_booking()[0].check_out_date
        context['last_booking'] = Booking.objects.last().id
        context['length'] = len(self.get_booking())
        return context


def next_room(request, room_id, booking_id, last_booking, length):
    booking = get_object_or_404(Booking, id=booking_id)
    room = get_object_or_404(Room, id=room_id)
    rooms_to_remove = booking.rooms.exclude(id=room.id)
    for room in rooms_to_remove:
        booking.rooms.remove(room)

    booking.is_approved = True
    booking.save()
    if booking_id + 1 <= last_booking:
        return render(request, 'users/rooms.html', {'booking': Booking.objects.get(id=booking_id+1), 'last_booking' : last_booking, 'length' : length})
    else:
        last_booking += 1
        return render(request, 'users/check_out.html', {'bookings' : [Booking.objects.get(id=num) for num in range(last_booking - length, last_booking)]})


class CheckOut(ListView):
    template_name = 'users/check_out.html'
    model = Booking