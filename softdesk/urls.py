
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views  import TokenObtainPairView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('custom_user.urls')),
    path('project/', include('project.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    
]
