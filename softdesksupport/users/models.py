from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from resources.models import Project


class User(AbstractUser):
    age = models.PositiveIntegerField()
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()

    def __str__(self):
        return self.username
        


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributing'
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='contributors'
    )
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} contributed to project {self.project}"

    class Meta:
        unique_together = (
            "user",
            "project",
        )

