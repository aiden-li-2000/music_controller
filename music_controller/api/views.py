from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() # data we want to return 
    serializer_class = RoomSerializer   # in which format
