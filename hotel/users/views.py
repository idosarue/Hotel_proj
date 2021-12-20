from django.contrib.auth.models import GroupManager
from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView
from .forms import RoomsDateForm, GuestsFormSet
from .models import Room
from django.contrib import messages

class Home(FormView):
    template_name = 'users/home.html'
    form_class = RoomsDateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = GuestsFormSet
        return context       

class RoomsResults(ListView):
    template_name = 'users/rooms.html'
    model = Room
    
    def get(self, request, *args, **kwargs):
        form = RoomsDateForm(request.GET)
        formset = GuestsFormSet(request.GET)
        if not form.is_valid() or not formset.is_valid():
            return render(request,'users/home.html', {'form' : form, 'formset' : formset})
        return super().get(request, *args, **kwargs)

    def get_data(self):
        get_request = self.request.GET
        form = RoomsDateForm(self.request.GET)
        formset = GuestsFormSet(get_request)
        for form in formset:
            if form.is_valid():
                print(form.cleaned_data)
        if form.is_valid() and formset.is_valid():
            rooms = [{'children' : get_request[f'form-{num}-children'], 'adults' : get_request[f'form-{num}-adults']} for num in range(int(get_request['form-TOTAL_FORMS']))]
            return rooms
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.get_data()
        return context

