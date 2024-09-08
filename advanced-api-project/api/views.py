# api.py

from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of all books or create a new book.

    GET: Retrieves a list of all books.
    POST: Creates a new book instance.

    Permissions:
    - GET: Allows any user (authenticated or not) to access the list.
    POST: Only authenticated users can create new books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific book.
    
    GET: Retrieves details of a specific book.
    PUT/PATCH: Updates a specific book.
    DELETE: Deletes a specific book.

    Permissions:
    - GET: Allow any user (authenticated or not) to retrieve book details.
    - PUT/PATCH/DELETE: Only authenticated users can modify or delete books.
    """

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]