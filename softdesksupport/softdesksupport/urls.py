"""
URL configuration for softdesksupport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserRegistrationView, ContributorViewSet
from resources.views import (
    ProjectViewSet,
    IssueViewSet,
    CommentViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'issues', IssueViewSet, basename='issues')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'contributors', ContributorViewSet, basename='contributors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Separate URL for registering users, this is not part of the router
    path('register/', UserRegistrationView.as_view(), name='register'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
