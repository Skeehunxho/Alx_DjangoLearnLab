from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from .models import Library 
from django.views.generic.detail import DetailView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view: show details of a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log them in after registration
            return redirect('login')  # You can redirect to another page if you prefer
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

