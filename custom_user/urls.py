from django.urls import path


from custom_user import views


urlpatterns = [path("signup/", views.RegisterApi.as_view())]
