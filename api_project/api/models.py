# models.py

from django.db import models


class Book(models.Model):
    """
    Class representing a book
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.title