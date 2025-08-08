import os
import sys
import django

# --- Ensure we can import Django settings no matter where we run the script ---
# Get the absolute path to the project root (where manage.py is located)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add project root to Python path
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')

# Setup Django
django.setup()

# Now you can import your models
from relationship_app.models import Book

# --- Sample queries ---
def run_queries():
    print("All Books:")
    for book in Book.objects.all():
        print(f"- {book.title} by {book.author}")

if __name__ == "__main__":
    run_queries()
