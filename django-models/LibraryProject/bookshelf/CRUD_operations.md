# CRUD Operations

# Create Book
>>> ...
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
# Output: 1984

# Retrieve Book
>>> ...
>>> book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949

# Update Book Title
>>> ... 
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
# Output: Nineteen Eighty-Four

# Delete Book
>>> from bookshelf.models import Book
>>> book.delete()
>>> book = Book.objects.first()
>>> Book.objects.filter(id=1).delete()
(0, {})
>>> books = Book.objects.all()
>>> print(list(books))
# Output: []