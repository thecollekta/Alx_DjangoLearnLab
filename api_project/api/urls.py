# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet
from .views import BookList

# Router and BokViewSet registration
router = DefaultRouter()
router.register(r'books', BookViewSet)

# API URLs to be determined by router
urlpatterns = [
    path('', include(router.urls)),
    # path('books/', BookList.as_view(), name='book_list'),
]
