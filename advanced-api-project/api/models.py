# models.py

from django.db import models


class Author(models.Model):
    """
    Represents an author in the system.

    This model stores information about authors of books. Each author can have
    multiple books associated with them, establishing a one-to-many relationship
    with the Book model.

    Fields:
    - name: A CharField to store the author's full name.

    Relationships:
    - books: A reverse relationship to the Book model. This allows easy access
             to all books written by this author.
    """

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    """
    Represents a book in the system.

    This model stores information about individual books. Each book is 
    associated with one author, creating a many-to-one relationship 
    with the Author model.

    Fields:
    - title: A CharField to store the book's title.
    - publication_year: An IntegerField to store the year the book was published.
    - author: A ForeignKey linking to the Author model. This establishes the
              many-to-one relationship between Book and Author.

    Relationships:
    - author: Links each book to its author. The 'on_delete=models.CASCADE' means
              if an author is deleted, all their books will be deleted as well.
              The 'related_name' allows reverse lookup from Author to Books.
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, 
                               related_name='books')

    def __str__(self):
        return self.title