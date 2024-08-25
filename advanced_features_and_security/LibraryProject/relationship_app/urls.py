from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register
from .views import TemplateView
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='admin_view'),
    path('member/', member_view, name='admin_view'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(template_name='relationship_app/library_detail.html'), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('', TemplateView.as_view(template_name="relationship_app/home.html"), name='home'),
]