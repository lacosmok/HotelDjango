from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'), max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label=_('Password'), max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
