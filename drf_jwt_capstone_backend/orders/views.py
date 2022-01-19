from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderCreateSerializer, OrderViewSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderViewSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_orders(request):
    if request.method == 'POST':
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        orders = Order.objects.filter(user_id = request.user.id)
        serializer = OrderViewSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        orders = Order.objects.filter(user_id = request.user.id)
        for order in orders:
            order = order
        serializer = OrderCreateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orders = Order.objects.filter(user_id = request.user.id)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_status(request, pk):
    order = Order.objects.filter(id = pk).first()
    serializer = OrderCreateSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)