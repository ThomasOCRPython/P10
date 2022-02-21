from django.db import models
from django.conf import settings
from custom_user.models import User


class Project(models.Model):

    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    IOS = "IOS"
    ANDROID = "ANDROID"
    PROJECT_TYPES = (
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    )

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=9, choices=PROJECT_TYPES)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Contributor(models.Model):

    CHOICES = (("NO", "NO"), ("YES", "YES"))
    ROLES = (("AUTHOR", "AUTHOR"), ("CONTRIBUTOR", "CONTRIBUTOR"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=3, choices=CHOICES)
    role = models.CharField(max_length=11, choices=ROLES)


class Issue(models.Model):

    PRIORITY = (("FAIBLE", "FAIBLE"), ("MOYENNE", "MOYENNE"), ("ELEVEE", "ELEVEE"))
    TAG = (("BUG", "BUG"), ("AMELIORATION", "AMELIORATION"), ("TÂCHE", "TÂCHE"))
    STATUS = (("A FAIRE", "A FAIRE"), ("EN COURS", "EN COURS"), ("TERMINE", "TERMINE"))

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    tag = models.CharField(max_length=120, choices=TAG)
    priority = models.CharField(max_length=120, choices=PRIORITY)
    project_id = models.IntegerField(null=True)
    status = models.CharField(max_length=120, choices=STATUS)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee_user = models.ForeignKey(Contributor, null=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    description = models.CharField(max_length=120)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
