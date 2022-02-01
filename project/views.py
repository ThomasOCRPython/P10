from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project import serializers, models
from project.permissions import IsOwnerOrReadOnly, IsOwnerOrContributor
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAdminAuthenticated




class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ProjectListSerializer
    # detail_serializer_class = serializers.ProjectDetailSerializer

    def get_queryset(self):
        return  models.Project.objects.all()

    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
       
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).update(request, *args, **kwargs)

class ContributorViewset(viewsets.ModelViewSet):

    # test = get_object_or_404(models.Contributor, id= project_id)
    # print(test)
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ContributorSerializer

    def get_queryset(self):
        return  models.Contributor.objects.all()

    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        print(kwargs,11111111,args)
        request.data["project"] = self.kwargs["project_pk"]
        request.POST._mutable = False
        return super(ContributorViewset, self).create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
        
    #     print(kwargs,11111111,args)
    #     request.POST._mutable = True
    #     request.data["project"] = self.kwargs["project_pk"]
    #     request.POST._mutable = False
    #     return super(ContributorViewset, self).update(request, *args, **kwargs)
    

class IssueViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrContributor]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.IssueSerializer
    

    def get_queryset(self):
        return  models.Issue.objects.all()

    def create(self, request, *args, **kwargs):
        
        
        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project_pk"]
        request.data["assignee_user"] = request.user.pk
        request.POST._mutable = False
        return super(IssueViewset, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project_pk"]
        request.POST._mutable = False
        return super(IssueViewset, self).update(request, *args, **kwargs)

class CommentViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.CommentSerializer
    

    def get_queryset(self):
        return  models.Comment.objects.all()

    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        print(kwargs,11111111,args)
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = self.kwargs["issues_pk"]
        request.POST._mutable = False
        return super(CommentViewset, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        print(kwargs,11111111,args)
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = self.kwargs["issues_pk"]
        return super(CommentViewset, self).update(request, *args, **kwargs)


