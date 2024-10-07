# library_management_system/accounts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet, LogoutViewSet, CustomUserViewSet

router = DefaultRouter()
router.register('register', UserViewSet, basename='register')
router.register('login', LoginViewSet, basename='login')
router.register('logout', LogoutViewSet, basename='logout')
router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
   path('', include(router.urls)),
]