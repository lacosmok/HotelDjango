from django.views.generic import ListView, TemplateView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from rest_framework import viewsets, views, generics, status
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Hotel, Reservation, Room, Profile, Address, Telephone
from .forms import UserForm, ReservationForm, ProfileEditForm
from .serializers import HotelSerializer, ReservationSerializer, RoomSerializer, ProfileSerializer

import operator
from datetime import datetime

PAGINATE_BY = 2


# New views


class ApiHotelListView(TemplateView):
    template_name = "rest/hotel_list.html"


@method_decorator(login_required, name='dispatch')
class ApiRoomListView(TemplateView):
    template_name = "rest/room_list.html"


@method_decorator(login_required, name='dispatch')
class ApiProfileView(TemplateView):
    template_name = "rest/user_profile.html"


# Old views


class ReservationCreateAPIView(generics.CreateAPIView):
    serializer_class = ReservationSerializer


@method_decorator(login_required, name='dispatch')
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "registration_form.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ReservationCreateView, self).get_context_data(**kwargs)
        context['reservation_create'] = True
        return context

    def get_form_kwargs(self, **kwargs):
        kwargs = super(ReservationCreateView, self).get_form_kwargs()
        kwargs['room_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form, **kwargs):
        context = super(ReservationCreateView, self).form_valid(form, **kwargs)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.room = Room.objects.get(pk=self.kwargs['pk'])
        self.object.save()
        return context


class HotelListView(ListView):
    template_name = "hotel_list.html"
    paginate_by = PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super(HotelListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Hotel.objects.all()


@method_decorator(login_required, name='dispatch')
class RoomListView(ListView):
    model = Room
    template_name = "room_list.html"
    paginate_by = PAGINATE_BY

    def get_context_data(self, **kwargs):
        context = super(RoomListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(hotel__pk=self.kwargs["pk"])


class UserFormView(View):
    form_class = UserForm
    template_name = "registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            address = Address.objects.create()
            telephone = Telephone.objects.create()
            Profile.objects.create(user=user, addres=address,
                                   telephone=telephone)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('rest-hotel-list')


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = "user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(
            user=self.request.user)
        context['reservations'] = Reservation.objects.filter(user=self.request.user)
        return context


class ProfileEditView(View):
    form_class = ProfileEditForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            profile = Profile.objects.get(
                user=self.request.user)
            # profile.photo = form.cleaned_data['photo']
            profile.name = form.cleaned_data['name']
            telephone = profile.telephone
            telephone.nr = form.cleaned_data['telephone']
            address = profile.addres
            address.street = form.cleaned_data['street']
            address.nr = form.cleaned_data['street_nr']
            address.city = form.cleaned_data['city']
            address.save()
            profile.save()
            telephone.save()
        return redirect('user-profile')


class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('user-profile')


class HotelSearchView(HotelListView):
    def get_queryset(self):
        result = super(HotelSearchView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list))
            )
        return result


# REST Framework views


class HotelListAPIView(views.APIView):
    def get(self, request):
        queryset = Hotel.objects.all()
        serializer = HotelSerializer(queryset, many=True)
        return Response({'hotels': serializer.data})


class RoomListAPIView(views.APIView):
    """
     A view that returns a templated HTML representation of room list.
    """

    def get(self, request, pk):
        queryset = Room.objects.filter(hotel__pk=pk)
        serializer = RoomSerializer(queryset, many=True)
        return Response({'rooms': serializer.data})

    def post(self, request, pk):
        request.data['start_date'] = datetime.strptime(request.data.get('start_date', None), '%Y-%m-%d').date()
        request.data['end_date'] = datetime.strptime(request.data['end_date'], '%Y-%m-%d').date()
        request.data['user'] = self.request.user.pk
        serializer = ReservationSerializer(data=request.data)
        if not serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            raise ValidationError
        serializer.save()
        return Response({'rooms': serializer.data})


class ProfileApiView(views.APIView, DestroyModelMixin):
    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        profile_serializer = ProfileSerializer(profile)
        queryset = Reservation.objects.filter(user=self.request.user)
        serializer = ReservationSerializer(queryset, many=True)
        return Response({'reservations': serializer.data, "profile": profile_serializer.data})


class ReservationDestroyApiView(generics.DestroyAPIView):
    def delete(self, request,pk):
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
