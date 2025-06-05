from django.urls import path
from users import views

urlpatterns = [
     path('users', views.UserViewSet, name='users'),
     path('register/', views.UserRegistrationView.as_view(), name='register'),
     path('contributors', views.ContributorViewSet.as_view(), name='contributors')
]