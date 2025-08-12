from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted")
print("All books:", Book.objects.all())
# Expected output:
# Book deleted
# All books: <QuerySet []>