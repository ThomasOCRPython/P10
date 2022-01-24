from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProjectSerializer
from .models import Project
from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAdminAuthenticated




class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    # permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminAuthenticated]

    