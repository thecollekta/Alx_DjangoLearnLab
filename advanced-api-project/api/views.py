# api.py

from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of all books with filtering, searching, and 
    ordering capabilities.
    
    GET: Retrieves a list of all books.

    Permissions:
    - GET: Allow any user (authenticated or not) to access the list.

    Filtering:
    - Can filter by 'title', 'author', and 'publication_year'

    Searching:
    - Can search in 'title' and 'author' fields

    Ordering:
    - Can order by 'title', 'publication_year', and 'author'
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year'] #Fields to filter
    search_fields = ['title', 'author'] # Specific search fields
    ordering_fields = ['title', 'publication_year'] # Order fields
    ordering = ['title']  # default ordering



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