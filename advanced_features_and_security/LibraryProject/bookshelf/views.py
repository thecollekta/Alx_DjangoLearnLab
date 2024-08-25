# bookshelf/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView
from django.utils.decorators import decorator_from_middleware
from csp.middleware import CSPMiddleware
from .forms import ExampleForm
from .forms import BookSearchForm

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'bookshelf/edit_book.html'
    permission_required = 'bookshelf.can_edit'

# With this view, a user can have the "can_edit" permission.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    #Logic for editing book
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Validation and sanitisation
@decorator_from_middleware(CSPMiddleware)
def book_list(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all() # All book instances retrieval
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

def search_books(request):
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'bookshelf/book_list.html', {'books': books})
        else:
            # Form invalid data
            pass

# Content Security Policy (CSP) implementation
def secure_view(request):
    response = render(request, 'bookshelf/book_list.html')
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trustedscripts.example.com;"
    return response