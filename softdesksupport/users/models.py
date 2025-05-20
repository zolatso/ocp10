from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from resources.models import Project


class User(AbstractUser):
    age = models.PositiveIntegerField(default=15)
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)

    def __str__(self):
        return self.username
        


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributing"
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="contributors",
    )
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (
            "user",
            "project",
        )

