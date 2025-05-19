from django.db import models
from django.conf import settings

class Project(models.Model):
    TYPE_CHOICES = [
        ("back-end", "back-end"),
        ("front-end", "front-end"),
        ("iphone", "iphone"),
        ("android", "android"),
    ]
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(
        max_length=9,
        choices=TYPE_CHOICES)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="authored_projects"
    )
    time_created = models.DateField(auto_now_add=True)
