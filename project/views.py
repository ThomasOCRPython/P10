
from rest_framework import viewsets

from project import serializers, models
from project.permissions import (
    IsContributorOrAuthorProjectInIssueView,
    IsContributorOrAuthorProjectInProjectView,
    IsContributorOrAuthorProjectInContributorView,
    IsContributorOrAuthorProjectInCommentView
)

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsContributorOrAuthorProjectInProjectView]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ProjectListSerializer
    

    def get_queryset(self):
        
        return models.Project.objects.filter(
            Q(author_user_id=self.request.user.id) | Q(contributor__user=self.request.user.id)
        )

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

    permission_classes = [IsAuthenticated,IsContributorOrAuthorProjectInContributorView]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.ContributorSerializer

    
    def get_queryset(self):
        
        return models.Contributor.objects.filter(project=self.kwargs["project_pk"])
                

    def create(self, request, *args, **kwargs):

        request.POST._mutable = True
        request.data["project"] = self.kwargs["project_pk"]
        request.POST._mutable = False
        return super(ContributorViewset, self).create(request, *args, **kwargs)


class IssueViewset(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated, IsContributorOrAuthorProjectInIssueView]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.IssueSerializer

    def get_queryset(self):

        return models.Issue.objects.filter(
            (
                
                Q(project_id=self.request.user.id)
                | Q(assignee_user=self.request.user.id)
            )
            
        )

    def create(self, request, *args, **kwargs):
        

        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project_pk"]
        request.data["author_user_id"]=request.user.pk
        request.data["assignee_user"] = request.user.pk
        request.POST._mutable = False
        return super(IssueViewset, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project_pk"]
        request.POST._mutable = False
        return super(IssueViewset, self).update(request, *args, **kwargs)


class CommentViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsContributorOrAuthorProjectInCommentView]

    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.CommentSerializer

    
    def get_queryset(self):
        
        return models.Comment.objects.filter(Q(issue_id=self.kwargs["issues_pk"]) | Q(author_user=self.request.user.id))

    def create(self, request, *args, **kwargs):

        request.POST._mutable = True
        request.data["author_user"] = request.user.pk
        request.data["issue_id"] = kwargs["issues_pk"]
        request.POST._mutable = False
        return super(CommentViewset, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user"] = request.user.pk
        request.data["issue_id"] = kwargs["issues_pk"]
        return super(CommentViewset, self).update(request, *args, **kwargs)
