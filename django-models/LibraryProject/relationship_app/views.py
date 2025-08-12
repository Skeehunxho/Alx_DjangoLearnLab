from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Library, Librarian

# View to list all authors
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'relationship_app/author_list.html', {'authors': authors})

# View to display books for a specific author
def author_books(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'relationship_app/author_books.html', {'author': author, 'books': books})

# View to list all libraries
def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

# View to display librarian details for a specific library
def librarian_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    librarian = getattr(library, 'librarian', None)  # OneToOne relation
    return render(request, 'relationship_app/librarian_detail.html', {'library': library, 'librarian': librarian})
