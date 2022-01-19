from rest_framework import serializers
from .models import Order
from lunchgroups.models import LunchGroup

class OrderSerializer(serializers.ModelSerializer):
    lunchgroup = serializers.PrimaryKeyRelatedField(queryset=LunchGroup.objects.all())
    class Meta:
        model = Order
        fields = ['id', 'lunchgroup', 'user_id', 'order_content', 'price', 'notes', 'status']
        depth = 1