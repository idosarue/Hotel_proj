from django import forms
from django.forms import formset_factory, BaseFormSet

class DateInput(forms.DateInput):
    input_type = 'date'

class RequiredFormSet(BaseFormSet):
    def clean(self):
        for form in self.forms:
            if not form.has_changed():
                raise forms.ValidationError('Please add at least one vehicle')
class GuestsForm(forms.Form):
    adults = forms.IntegerField(required=True)
    children = forms.IntegerField()


class RoomsDateForm(forms.Form):
    check_in_date = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'check_in_date'}))
    check_out_date = forms.DateField(widget=forms.HiddenInput(attrs={'id': 'check_out_date'}))

    # def clean(self):
    #     data = self.cleaned_data
    #     if data['check_in_date'] > data['check_out_date']:
    #         raise forms.ValidationError('Check in date must be after check out date.')
    #     return data



GuestsFormSet = formset_factory(GuestsForm, extra=1, formset= RequiredFormSet)