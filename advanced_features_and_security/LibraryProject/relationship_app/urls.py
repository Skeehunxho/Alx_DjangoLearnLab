from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth import views as auth_views


app_name = 'relationship_app'

urlpatterns = [
    # function-based view
    path('books/', views.list_books, name='list_books'),

    # class-based view (DetailView for a Library)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
urlpatterns = [
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    
    # Add Book
    path('add_book/', views.add_book, name='book_add'),
    
    # Edit Book
    path('edit_book/<int:book_id>/', views.edit_book, name='book_edit'),
    
    # Delete Book
    path('delete_book/<int:book_id>/', views.delete_book, name='book_delete'),
]
