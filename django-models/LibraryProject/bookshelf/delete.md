# delete.md

# Delete Book
>>> from bookshelf.models import Book
>>> book.delete()
>>> book = Book.objects.first()
>>> Book.objects.filter(id=1).delete()
(0, {})
>>> books = Book.objects.all()
>>> print(list(books))
# Output: []