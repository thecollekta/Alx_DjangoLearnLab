# blog/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from blog import views as user_login
from .views import (homepage, PostListView, PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, CommentCreateView, 
                    CommentUpdateView, CommentDeleteView, search_posts)

urlpatterns = [
    # User authentication
    path('register/', user_login.register, name='register'),
    path('profile/', user_login.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'), 
    # Post list/detail view and CRUD operations for posts
    path('', homepage, name='home'), # Homepage URL
    path('posts/', PostListView.as_view(), name='posts'), # Blog Posts list
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment CRUD operations
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), 
         name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), 
         name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), 
         name='delete-comment'),

    # Search functionality and filtering posts by tag
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), 
         name='posts-by-tag'),  # Posts filtered by tag
]