# serializers.py

from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer handles the conversion of Book model instances to JSON format
    and vice versa. It includes custom validation for the publication_year field.

    Fields:
    - id: Automatically included by ModelSerializer.
    - title: The book's title.
    - publication_year: The year the book was published.
    - author: The ID of the author (foreign key).

    Validation:
    - Ensures that the publication_year is not set to a future date.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation method for publication_year.

        Ensures that the publication year is not set in the future.

        Args:
            value (int): The publication year to validate.

        Returns:
            int: The validated publication year.

        Raises:
            serializers.ValidationError: If the year is in the future.
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be a future date.")
        return value
        """

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer handles the conversion of Author model instances to JSON format
    and vice versa. It includes a nested representation of the author's books.

    Fields:
    - id: Automatically included by ModelSerializer.
    - name: The author's name.
    - books: A nested serialization of all books by this author.

    The 'books' field uses the BookSerializer to provide a detailed representation
    of each book associated with the author. This creates a nested structure in 
    the serialized data, allowing for a comprehensive view of an author and their works.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']