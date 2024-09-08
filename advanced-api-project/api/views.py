# api.py

from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of all books.
    
    GET: Retrieves a list of all books.

    Permissions:
    - GET: Allow any user (authenticated or not) to access the list.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    
    POST: Creates a new book instance.

    Permissions:
    - POST: Only authenticated users can create new books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a specific book.
    
    GET: Retrieves details of a specific book.

    Permissions:
    - GET: Allow any user (authenticated or not) to retrieve book details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update a specific book.
    
    PUT/PATCH: Updates a specific book.

    Permissions:
    - PUT/PATCH: Only authenticated users can modify books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a specific book.
    
    DELETE: Deletes a specific book.

    Permissions:
    - DELETE: Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]