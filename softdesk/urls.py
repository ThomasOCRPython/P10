
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views  import TokenObtainPairView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom_user.urls')),
    path('', include('project.urls')),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    
    
]
