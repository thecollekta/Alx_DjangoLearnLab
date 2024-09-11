# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, 
                    CommentCreateView, CommentUpdateView, CommentDeleteView)

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:comment_id>/edit/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
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