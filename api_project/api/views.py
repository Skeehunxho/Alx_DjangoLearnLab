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

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
