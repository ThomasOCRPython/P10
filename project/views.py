from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project import serializers, models
from project.permissions import IsOwnerOrReadOnly,IsIssueOwnerOrReadOnly, IsCommentOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated





class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ProjectListSerializer
    # detail_serializer_class = serializers.ProjectDetailSerializer

    def get_queryset(self):
        # return models.Project.objects.filter(contributor__user=self.request.user.id)
        return models.Project.objects.filter(Q(author_user_id=request.user.id)|Q(contributor=request.user.id))
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

    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ContributorSerializer

    def get_queryset(self):
        return  models.Contributor.objects.all()

    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
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
    permission_classes = [IsAuthenticated, IsIssueOwnerOrReadOnly]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.IssueSerializer
    

    def get_queryset(self):
        return  models.Issue.objects.all()
    
    # def get_queryset(self):
    #     project_id = self.kwargs['project_pk']
    #     project = (Project.objects.filter(pk=project_id,
    #                                       project_contributor__user=self.request.user)
    #                | Project.objects.filter(pk=project_id, author_user_id=self.request.user))

    #     return project[0].issue_related

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
    permission_classes = [IsAuthenticated, IsCommentOwnerOrReadOnly]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.CommentSerializer
    

    def get_queryset(self):
        return  models.Comment.objects.all()

    def create(self, request, *args, **kwargs):
        
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = self.kwargs["issues_pk"]
        request.POST._mutable = False
        return super(CommentViewset, self).create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.data["issue_id"] = self.kwargs["issues_pk"]
        return super(CommentViewset, self).update(request, *args, **kwargs)


