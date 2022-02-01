from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from project import views

from rest_framework_nested import routers 



projects_router = routers.SimpleRouter(trailing_slash=False)
projects_router.register(r"project/?", views.ProjectViewSet, basename='project')

users_router = routers.NestedSimpleRouter(projects_router, r"project/?", lookup="project")
users_router.register(r"users/?", views.ContributorViewset, basename="users" )

issues_router = routers.NestedSimpleRouter(projects_router, r"project/?", lookup="project")
issues_router.register(r"issues/?", views.IssueViewset, basename="issues", )

comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues")
comments_router.register(r"comments/?", views.CommentViewset, basename="comments", )

urlpatterns = [
    path('',include(projects_router.urls)),
    path('',include(users_router.urls)),
    path('',include(issues_router.urls)),
    path('',include(comments_router.urls)),
]