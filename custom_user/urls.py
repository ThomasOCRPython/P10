from django.urls import path, include
from rest_framework.routers import DefaultRouter
from custom_user import views

router =  DefaultRouter()
router.register('custom-user', views.CustomUserViewSet, basename='custom-user')
urlpatterns = [
    path('',include(router.urls))
]