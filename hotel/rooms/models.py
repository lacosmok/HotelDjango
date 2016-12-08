from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Reservation(models.Model):
    reservation_start = models.DateField(null=False, default=now,
                                         verbose_name='start of reservation')
    reservation_finish = models.DateField(null=False, default=now,
                                          verbose_name='end of reservation')


class Profile(models.Model):
    pass


class Addres(models.Model):
    street = models.CharField(max_length=60, default='', blank=True, null=True)
    nr = models.IntegerField(default=0, verbose_name="number")
    city = models.CharField(max_length=60, default='', blank=True, null=True)

    def __str__(self):
        return "{} {} nr. {}".format(self.city, self.street, self.nr)


class Telephone(models.Model):
    telephone_nr = models.IntegerField(default=0,
                                       verbose_name="telephone number")


class Hotel(models.Model):
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    #address = models.ForeignKey(Addres, null=True, blank=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default='', blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)


