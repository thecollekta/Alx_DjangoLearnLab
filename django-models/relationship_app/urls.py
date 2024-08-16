from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]