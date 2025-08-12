from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/books/', views.author_books, name='author_books'),
    path('libraries/', views.library_list, name='library_list'),
    path('libraries/<int:library_id>/librarian/', views.librarian_detail, name='librarian_detail'),
]
