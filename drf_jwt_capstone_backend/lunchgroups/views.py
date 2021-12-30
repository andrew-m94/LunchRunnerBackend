from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import LunchGroup
from .serializers import LunchGroupSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_lunch_groups(request):
    lunch_groups = LunchGroup.objects.all()
    serializer = LunchGroupSerializer(lunch_groups, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def runner_lunch_group(request):
    if request.method == 'POST':
        serializer = LunchGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        groups = LunchGroup.objects.filter(user_id = request.user.id)
        serializer = LunchGroupSerializer(groups, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        groups = LunchGroup.objects.filter(user_id = request.user.id)
        for group in groups:
            group = group
        serializer = LunchGroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        groups = LunchGroup.objects.filter(user_id = request.user.id)
        groups.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)