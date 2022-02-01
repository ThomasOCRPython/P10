
from rest_framework import permissions
from project import models, views
from django.shortcuts import get_object_or_404
from django.db.models import Q
# return models.Project.objects.filter(Q(author_user_id=request.user)|Q(contributor=request.user))

class IsOwnerOrReadOnly(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            
            return True
        
        return obj.author_user_id == request.user


class IsOwnerOrContributor(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            
            return True
        
        return models.Project.objects.filter(Q(author_user_id=request.user)|Q(contributor=request.user))
                
