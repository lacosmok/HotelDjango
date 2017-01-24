from rest_framework import serializers
from . import models


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = ('pk', 'photo', 'name', 'address', 'description')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('name', 'photo', 'description', 'pk')


class ReservationSerializer(serializers.ModelSerializer):
    room_name = serializers.SerializerMethodField('let_room_name')

    def let_room_name(self, res):
        room = models.Room.objects.get(pk=res.room.pk)
        return str(room.name)

    class Meta:
        model = models.Reservation
        fields = ('pk', 'start_date', 'end_date', 'room', 'user', 'room_name')

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")
        reservation_query = models.Reservation.objects.filter(room=data['room'])
        for reservation in reservation_query:
            if data['start_date'] <= reservation.end_date and reservation.start_date <= data['end_date']:
                raise serializers.ValidationError(
                    'Room is already reserved from ' + str(
                        reservation.start_date) +
                    ' to ' + str(reservation.end_date)
                    + ', please change date')
        return data

    def create(self, validated_data):
        return models.Reservation.objects.create(**validated_data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('street', 'nr', 'city')


class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telephone
        fields = 'nr'


class ProfileSerializer(serializers.ModelSerializer):
    telephone = TelephoneSerializer
    addres = AddressSerializer

    class Meta:
        model = models.Profile
        fields = ('user', 'photo', 'name', 'addres', 'telephone')
