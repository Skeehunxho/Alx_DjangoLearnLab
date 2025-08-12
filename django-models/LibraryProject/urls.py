from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # function-based view
    path('books/', views.list_books, name='list_books'),

    # class-based view (DetailView for a Library)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # or prefix with 'relationship/' if you prefer
]