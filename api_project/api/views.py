"""
Authentication & Permissions Setup:
- TokenAuthentication is enabled via settings.py
- Obtain tokens by POSTing username/password to /api-token-auth/
- By default, IsAuthenticatedOrReadOnly is applied:
  * Anyone can read (GET)
  * Only authenticated users can write (POST/PUT/DELETE)
"""

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.http import JsonResponse

from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return JsonResponse({
        "message": "Welcome to the API 🚀. Use /api/books/ to view books."
    })
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

