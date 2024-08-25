# bookshelf/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView

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