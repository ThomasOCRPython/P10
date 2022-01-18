from django.shortcuts import render
# from rest_framework import generics

from rest_framework import viewsets
from rest_framework.response import Response
from custom_user import serializers, models

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomUserSerializer
    queryset = models.CustomUser.objects.all()

