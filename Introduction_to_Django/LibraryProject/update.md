
# Retrieve a Book
from bookshelf.models import Book

retrieved_book = Book.objects.get(id=book.id)
retrieved_book

<Book: Nineteen Eighty Four by George Orwell(1949)>
