from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import NewUser, Profile
from django.utils.translation import gettext as _


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = NewUser
        fields = ('username', 'email')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'date_of_birth']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date', 'placeholder':'Select a date', 'required': True}),
            'phone_number': forms.DateInput(attrs={'required': True}),
        }

        labels = {
            "date_of_birth": _("date of birth"),
            "phone_number": _("Phone Number")
        }

    # def clean_date_of_birth(self):
    #     date_of_birth = self.cleaned_data['date_of_birth']
    #     if date_of_birth:
    #         if not calculateAge(date_of_birth):
    #             raise forms.ValidationError(_('you cannot sign up if you are younger than 18'))
    #     else:
    #         raise forms.ValidationError(_('please fill out this field'))
    #     return date_of_birth

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        print(phone_number)
        if Profile.objects.filter(phone_number=phone_number).exclude(user=self.instance.user).exists():
            raise forms.ValidationError(_('phone exists'))
        return phone_number

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': _('username'), 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '*********',
        }
))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date', 'placeholder':'Select a date','required': True}),
            'phone_number': forms.DateInput(attrs={'required': True}),
        }

        labels = {
            "date_of_birth": _("date of birth"),
            "phone_number": _("Phone Number")
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(_('phone exists'))
        return phone_number