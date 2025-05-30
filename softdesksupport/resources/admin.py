from django.contrib import admin
from resources.models import Project, Issue, Comment

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Issue)
