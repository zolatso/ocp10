from django.urls import path, include
from rest_framework.routers import DefaultRouter

from resources import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]