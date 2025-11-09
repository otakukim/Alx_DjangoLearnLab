# query_samples.py
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author using objects.filter
def books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    if books.exists():
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    else:
        print(f"No books found by {author_name}")

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# 3. Retrieve the librarian for a library using try/except
def librarian_of_library(library_name):
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"The librarian of {library_name} is {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

# Example usage
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
