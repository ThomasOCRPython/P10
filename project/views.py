from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project import serializers, models

from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAdminAuthenticated




class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ProjectListSerializer
    detail_serializer_class = serializers.ProjectDetailSerializer

    def get_queryset(self):
        return  models.Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'intreve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    



       