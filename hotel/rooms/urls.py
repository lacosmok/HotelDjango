from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HotelListView.as_view(), name='index'),
    url(r'^$', views.HotelSearchView.as_view(), name='hotel-search'),
    url(r'^hotels/(?P<pk>[0-9]+)/rooms/$',
        views.RoomListView.as_view(), name='room-list'),
    url(r'^rooms/(?P<pk>[0-9]+)/reservation/$',
        views.ReservationCreateView.as_view(), name='reservation-create'),
    url(r'^profile/$', views.ProfileView.as_view(), name='user-profile'),
    url(r'^register/$', views.UserFormView.as_view(), name='register-user'),
    url(r'^reservations/(?P<pk>[0-9]+)/$',
        views.ReservationDeleteView.as_view(), name='reservation-delete'),
]