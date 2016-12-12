from django.contrib.auth.models import User
from django import forms
from .models import Reservation
from django.contrib.admin import widgets

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ["end_date", "start_date"]
"""
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
"""