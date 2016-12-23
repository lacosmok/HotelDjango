from rest_framework import serializers

from . import models


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Hotel
        fields = ('photo', 'name', 'addres', 'description', )


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = ('start_date', 'end_date')
