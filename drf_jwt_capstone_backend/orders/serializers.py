from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'lunchgroup', 'user_id', 'order_content', 'price', 'notes']