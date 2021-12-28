from django.contrib.auth.models import GroupManager
from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from .forms import RoomsDateForm, GuestsFormSet
from .models import Room
from django.contrib import messages
from django.http import JsonResponse, request
from .search_validation import validate_guests, validate_dates

class Home(FormView):
    template_name = 'users/home.html'
    form_class = RoomsDateForm

    def form_invalid(self, form):
        print('invalid')
        return JsonResponse({"error": form.errors}, status=400)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['formset'] = GuestsFormSet
    #     return context       

class RoomsResults(ListView):
    template_name = 'users/rooms.html'
    model = Room


    def get_date(self):
        return validate_dates(self.request.GET)

    def get_data(self):
        # get_request = self.request.GET
        return validate_guests(self.request, int(f'{self.request.GET}'.count('room')) // 2)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.get_data() 
        context['check_in_date'] = self.get_date()['check_in_date']
        context['check_out_date'] = self.get_date()['check_out_date']
        return context

