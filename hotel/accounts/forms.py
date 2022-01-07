from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import NewUser, Profile
from django.utils.translation import gettext as _

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].label = 'Confirm Password'

    class Meta:
        model = NewUser
        fields = ('username', 'email')

        widgets = {
            'password': forms.PasswordInput(attrs={'label': 'Confirm Password'}),
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = NewUser
        fields = ('username', 'email')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']

        widgets = {
            'phone_number': forms.DateInput(attrs={'required': True}),
        }

        labels = {
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
        attrs={'class': 'form-control', 'id': 'login_username', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id' : 'login_password'
        }
))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

        widgets = {
            'phone_number': forms.DateInput(attrs={'required': True}),
        }

        labels = {
            "phone_number": _("Phone Number")
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(_('phone exists'))
        return phone_number