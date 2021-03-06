import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Patient, Doctor


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is allowed in the range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to alwayas to return the cleaned data
        return data


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
