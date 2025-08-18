from django.urls import path
from .views import BookList, home

urlpatterns = [
    path('', home, name='home'),         # now root of /api/ shows a message
    path('books/', BookList.as_view(), name='book-list'),
]
