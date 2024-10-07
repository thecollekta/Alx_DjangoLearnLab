# library_management_system/accounts/tests.py

from django.test import TestCase
from .models import CustomUser
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

# Test for CustomUser Model
class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.is_active)
        self.assertEqual(self.user.role, CustomUser.MEMBER)

# Test for Views
class UserViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = CustomUser.objects.create_superuser(
            username='admin', 
            password='adminpass', 
            email='admin@example.com'
        )
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            password='password123', 
            email='test@example.com'
        )
        self.client.login(username='admin', password='adminpass')
