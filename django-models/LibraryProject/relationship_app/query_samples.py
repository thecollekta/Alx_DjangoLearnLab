from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author.
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# List all books in a library.
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


# Retrieve the librarian for a library.
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian