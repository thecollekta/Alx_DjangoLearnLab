# test_views.py

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year=2023, author=self.author)
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.book_list_url = reverse('book-list')

        # Log in the test client
        self.client.login(username='testuser', password='testpass123')

# CRUD Operations Tests
    def test_get_book_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_create_book(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Book', 'publication_year': 2024, 'author': self.author.pk}
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Book', 'publication_year': 2025, 'author': self.author.pk}
        response = self.client.put(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

# Filtering, Searching, and Ordering Tests
    def test_filtering(self):
        response = self.client.get(f'{self.book_list_url}?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(f'{self.book_list_url}?title=Non-existent Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_searching(self):
        response = self.client.get(f'{self.book_list_url}?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(f'{self.book_list_url}?search=Non-existent')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_ordering(self):
        Book.objects.create(title='Another Book', publication_year=2022, author=self.author)
        response = self.client.get(f'{self.book_list_url}?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')

        response = self.client.get(f'{self.book_list_url}?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')

# Authentication Tests
    def test_authentication_required(self):
        response = self.client.post(self.book_list_url, {'title': 'New Book', 'publication_year': 2024, 'author': self.author.pk})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(self.book_url, {'title': 'Updated Book', 'publication_year': 2025, 'author': self.author.pk})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)