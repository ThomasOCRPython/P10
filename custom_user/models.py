# from typing_extensions import Required
from django.db import models

# from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Vous devez entrer un email.')

#         user = self.model(
#                         email=self.normalize_email(email),
#                         )
#         user.set_password(password)

#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         user = self.create_user(email=email,
#                                 password=password,
#                                 )
#         # user.is_admin = True
#         # user.is_staff = True
#         user.save()
#         return user


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=128, blank=True)
#     last_name = models.CharField(max_length=128, blank=True)
#     email = models.EmailField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)

#     is_active = models.BooleanField(default=True)
#     # is_staff = models.BooleanField(default=False)
#     # is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELD = ['first_name','last_name']
#     objects = MyUserManager()

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True
class User(AbstractUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
