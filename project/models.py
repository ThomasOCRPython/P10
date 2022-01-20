from django.db import models
from django.conf import settings

class Project(models.Model):

    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    PROJECT_TYPES =(
        (BACKEND, 'Back-end'),
        (FRONTEND, 'Front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android')
    )

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=9, choices=PROJECT_TYPES)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE
                               )

    def __str__(self):
        return self.title
