from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Reservation(models.Model):
    reservation_start = models.DateField(null=False, default=now,
                                         verbose_name='start of reservation')
    reservation_finish = models.DateField(null=False, default=now,
                                          verbose_name='end of reservation')


class Profile(models.Model):
    id_profile = models.IntegerField(default=0, primary_key=True,
                                     verbose_name="room id")

    def __str__(self):
        return self.id_profile


class Addres(models.Model):
    id_addres = models.IntegerField(default=0, verbose_name="Addres id")

    def __str__(self):
        return self.id_addres


class Telephone(models.Model):
    id_telephone = models.IntegerField(default=0,
                                       verbose_name="telephone number")

    def __str__(self):
        return self.id_telephone


class Hotel(models.Model):
    id_hotel = models.IntegerField(default=0, verbose_name="hotel id")

    def __str__(self):
        return self.id_hotel


class Room(models.Model):
    id_room = models.IntegerField(default=0, verbose_name="room id")
    id_hotel = models.ForeignKey(Hotel, null=True, blank=True,
                                 verbose_name="hotel id")

    def __str__(self):
        return self.id_room
