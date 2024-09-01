# from django.shortcuts import render
from rest_framework.generics.ListAPIView import ListAPIView
from .models import Book
from .serializers import BookSerializer

# BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
