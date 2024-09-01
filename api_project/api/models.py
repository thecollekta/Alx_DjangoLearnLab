from django.db import models


class Book(models.Model):
    """Class representing a book"""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255)
