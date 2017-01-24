from django.conf.urls import url
from . import views

urlpatterns = [
    # New urls with rest
    url(r'^drf/$', views.ApiHotelListView.as_view(), name='drf-index'),
    url(r'^drf/hotels/(?P<pk>[0-9]+)/rooms/$',
        views.ApiRoomListView.as_view(), name='drf-room-list'),
    url(r'^drf/profile/$', views.ApiProfileView.as_view(), name='drf-user-profile'),
    # Old urls
    url(r'^$', views.HotelListView.as_view(), name='index'),
    url(r'^search/$', views.HotelSearchView.as_view(), name='hotel-search'),
    url(r'^hotels/(?P<pk>[0-9]+)/rooms/$',
        views.RoomListView.as_view(), name='room-list'),
    url(r'^rooms/(?P<pk>[0-9]+)/reservation/$',
        views.ReservationCreateView.as_view(), name='reservation-create'),
    url(r'^profile/$', views.ProfileView.as_view(), name='user-profile'),
    url(r'^profile/edit/$', views.ProfileEditView.as_view(),
        name='edit-user-profile'),
    url(r'^register/$', views.UserFormView.as_view(), name='register-user'),
    url(r'^reservations/(?P<pk>[0-9]+)/$',
        views.ReservationDeleteView.as_view(), name='reservation-delete'),
    # REST framework urls
    url(r'api/$', views.HotelListAPIView.as_view(), name='rest-hotel-list'),
    url(r'^api/hotels/(?P<pk>[0-9]+)/rooms/$',
        views.RoomListAPIView.as_view(), name='rest-room-list'),
    url(r'^api/profile/$', views.ProfileApiView.as_view(), name='rest-user-profile'),
    url(r'^api/reservations/(?P<pk>[0-9]+)/delete/$',
        views.ReservationDestroyApiView.as_view(), name='rest-reservation-delete'),

]
