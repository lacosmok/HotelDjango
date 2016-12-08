from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HotelListView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register-user'),
]