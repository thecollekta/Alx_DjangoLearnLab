from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLogoutView
from .views import register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # path('logout/', LogoutView.as_view(template_name='relationship_app/simple_logout.html'), name='logout'),
    # path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]