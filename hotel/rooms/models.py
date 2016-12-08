from __future__ import unicode_literals

from django.db import models

class Reservation(models.Model):
    pass

class Profile(models.Model):
    id_profile = models.IntegerField(default=0, verbose_name="room id")

class Addres(models.Model):
    id_addres = models.IntegerField(default=0, verbose_name="Addres id")

class Telephone(models.Model):
    id_telephone = models.IntegerField(default=0, verbose_name="telephone number")

class Hotel(models.Model):
    id_hotel = models.IntegerField(default=0, verbose_name="hotel id")

class Room(models.Model):
    id_room = models.IntegerField(default=0, verbose_name="room id")
    id_hotel = models.ForeignKey(Hotel, null=True, blank=True, verbose_name="hotel id")