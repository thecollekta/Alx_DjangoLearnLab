# social_media_api/accounts/urls.py

from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # For user registration
    path('login/', LoginView.as_view(), name='login'),  # For user login
    path('profile/', ProfileView.as_view(), name='profile'),  # For user profile management
]