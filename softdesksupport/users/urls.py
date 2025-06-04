from django.urls import path, include
from users import views

urlpatterns = [
     path('users', views.UserViewSet, name='users'),
     path('register/', views.UserRegistrationView.as_view(), name='register'),
]