import uuid
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

    def __str__(self):
        return self.title
    

class Issue(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1, "LOW"
        MEDIUM = 2, "MEDIUM"
        HIGH = 3, "HIGH"
    class IssueType(models.IntegerChoices):
        BUG = 1, "BUG"
        FEATURE = 2, "FEATURE"
        TASK = 3, "TASK"
    class Progress(models.IntegerChoices):
        TO_DO = 1, "To do"
        IN_PROGRESS = 2, "In progress"
        FINISHED = 3, "Finished"
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="issues_created"
    )
    project = models.ForeignKey(
        to='Project', 
        on_delete=models.CASCADE, 
        related_name="issues"
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    assigned_to = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="assigned_issues",
        blank=True,
        null=True
    )
    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM)
    issue_type = models.IntegerField(
        choices=IssueType.choices,
        default=IssueType.TASK)
    progress = models.IntegerField(
        choices=Progress.choices,
        default=Progress.TO_DO)
    time_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="comments_created"
    )
    issue = models.ForeignKey(
        to='Issue', 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    description = models.TextField(max_length=2048, blank=False)
    time_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title