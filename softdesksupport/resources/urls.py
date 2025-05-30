from django.urls import path, include
from resources import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('projects', views.ProjectViewSet, name='projects'),
    path('issues', views.IssueViewSet, name='issues'),
    path('comments', views.CommentViewSet, name='comments'),
]