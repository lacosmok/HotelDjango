from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Addres(models.Model):
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
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    addres = models.ForeignKey(Addres, null=True, blank=True)
    telephone = models.ForeignKey(Telephone, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Hotel(models.Model):
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    address = models.ForeignKey(Addres, null=True, blank=True)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    reservations = models.ManyToManyField(
        User,
        through='Reservation',
        through_fields=('room', 'user'),
    )
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
