from django.contrib.auth.views import logout, login
from django.conf.urls import url
from login.forms import LoginForm

from . import views


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
]
