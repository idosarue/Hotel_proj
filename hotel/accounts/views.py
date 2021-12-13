from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages



class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save()
        profile_form = ProfileForm(self.request.POST, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            user = authenticate(self.request, username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'] )   
            if user:
                login(self.request, user)
            else:
                messages.error(self.request, 'Something went wrong')
        else:
            user.delete()
            return self.form_invalid(form)

        return redirect('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm(self.request.POST or None)
        return context

class UserLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return redirect('home')
