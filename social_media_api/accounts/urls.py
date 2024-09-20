# social_media_api/accounts/urls.py

from django.urls import path
from .views import (RegisterView, LoginView, ProfileView, 
                    FollowUserView, UnfollowUserView)

urlpatterns = [

    # Registration/Login/Profile URLs
    path('register/', RegisterView.as_view(), name='register'), # User registration
    path('login/', LoginView.as_view(), name='login'), # User login
    path('profile/', ProfileView.as_view(), name='profile'), # User profile management

    # Follow/Unfollow URLs
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'), # Follow
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'), # Unfollow
]