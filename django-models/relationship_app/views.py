from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Function-based views implementation
def book_list(request):
    books = Book.objects.all()
    response_message = '\n'.join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response_message, content_type="text/plain")

# Class-based view implementation
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'