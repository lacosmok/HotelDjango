from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


def profile_directory_path(instance, filename):
    return 'profile_{0}/{1}'.format(instance.id, filename)


def hotel_directory_path(instance, filename):
    return 'hotel_{0}/{1}'.format(instance.id, filename)


def room_directory_path(instance, filename):
    return 'hotel_{0}/room_{1}'.format(instance.hotel.id, instance.id)


class Address(models.Model):
    street = models.CharField(max_length=60, default='', blank=True, null=True)
    nr = models.IntegerField(default=0, verbose_name="number")
    city = models.CharField(max_length=60, default='', blank=True, null=True)

    def __str__(self):
        return "{} {} nr. {}".format(self.city, self.street, self.nr)


class Telephone(models.Model):
    nr = models.IntegerField(default=0,
                             verbose_name="telephone number")


class Profile(models.Model):
    user = models.OneToOneField(
        User, default=None, null=True, blank=True,
        on_delete=models.CASCADE,
        # primary_key=True,
    )
    photo = models.ImageField(upload_to=profile_directory_path,
                              default='hotel_minimal_erd.png')
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    addres = models.ForeignKey(Address, null=True, blank=True)
    telephone = models.ForeignKey(Telephone, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Hotel(models.Model):
    photo = models.ImageField(upload_to=hotel_directory_path,
                              default='hotel_minimal_erd.png')
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    address = models.ForeignKey(Address, null=True, blank=True)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    reservations = models.ManyToManyField(
        User,
        through='Reservation',
        through_fields=('room', 'user'),
    )
    photo = models.ImageField(upload_to=room_directory_path,
                              default='hotel_minimal_erd.png')
    hotel = models.ForeignKey(Hotel, null=True, blank=True,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, default=None, null=True, blank=True,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, null=True, blank=True,
                             on_delete=models.CASCADE)
    start_date = models.DateField(null=False, default=now,
                                  verbose_name='start of reservation')
    end_date = models.DateField(null=False, default=now,
                                verbose_name='end of reservation')
