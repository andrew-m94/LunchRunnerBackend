from rest_framework import serializers
from .models import Order
from lunchgroups.models import LunchGroup

class OrderCreateSerializer(serializers.ModelSerializer):
    lunchgroup = serializers.PrimaryKeyRelatedField(queryset=LunchGroup.objects.all(), many=False)
    class Meta:
        model = Order
        fields = ['id', 'lunchgroup', 'user_id', 'order_content', 'price', 'notes', 'status']
        depth = 1

class OrderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'lunchgroup', 'user_id', 'order_content', 'price', 'notes', 'status']
        depth = 1