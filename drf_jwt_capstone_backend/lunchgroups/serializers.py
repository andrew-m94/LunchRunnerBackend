from rest_framework import serializers
from .models import LunchGroup

class LunchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchGroup
        fields = ['id', 'user_id', 'pickup_from', 'departure_time', 'drop_location', 'drop_time', 'private', 'invite_code']