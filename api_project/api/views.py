#views.py

from django.shortcuts import render
from rest_framework.generics import ListAPIView
# from rest_framework.generics.ListAPIView import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet to view and edit book instances.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()