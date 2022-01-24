from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from project import views
from rest_framework.routers import SimpleRouter

projects_router = routers.SimpleRouter()


router.register('project', views.ProjectViewSet, basename='project')
urlpatterns = [
    path('',include(router.urls))
]