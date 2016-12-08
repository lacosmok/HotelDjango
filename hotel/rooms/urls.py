from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HotelListView.as_view(), name='index'),
]