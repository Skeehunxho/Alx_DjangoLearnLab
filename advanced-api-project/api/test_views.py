from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create Author and Books
        self.author = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.id})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.id})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.id})

    # --- CRUD TESTS ---

    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_requires_authentication(self):
        """Test creating a book without authentication fails"""
        response = self.client.post(
            self.create_url,
            {"title": "Brave New World", "publication_year": 1932, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            self.create_url,
            {"title": "Brave New World", "publication_year": 1932, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        """Test updating a book when logged in"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.put(
            self.update_url,
            {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book_authenticated(self):
        """Test deleting a book when logged in"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- FILTERING / SEARCH / ORDERING TESTS ---

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 1949})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Animal"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.data[0]["title"], "1984")  # newest first

