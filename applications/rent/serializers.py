from rest_framework import serializers

from applications.rent.models import Rent


class RentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'


class RentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = [
            'title',
            'description',
            'address',
            'price',
            'rooms_count',
            'room_type'
        ]
