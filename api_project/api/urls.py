from django.urls import path
from .views import BookList, home

from django.urls import path
from .views import BookList, home

urlpatterns = [
    path('', home, name='home'),           # now /api/ shows welcome message
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, home

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', home, name='home'),                       # friendly landing
    path('books/', BookList.as_view(), name='book-list'),  # old list view
    path('', include(router.urls)),                   # all CRUD endpoints
]

