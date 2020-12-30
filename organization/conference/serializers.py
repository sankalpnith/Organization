from rest_framework import serializers
from .models import ConferenceRoom


class ConferenceRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConferenceRoom
        fields = (
            'id',
            'room_id',
            'booking_email',
            'name',
            'sitting_count',
            'status',
        )
        read_only_fields = (
            'id',
            'status',
        )
