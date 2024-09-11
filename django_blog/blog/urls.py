# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, 
                    CommentCreateView, CommentUpdateView, CommentDeleteView)

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # URL for adding a new comment to a post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    # URL for updating a comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    # URL for deleting a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]