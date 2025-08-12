from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # function-based view
    path('books/', views.list_books, name='list_books'),

    # class-based view (DetailView for a Library)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
