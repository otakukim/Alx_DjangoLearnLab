from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('advanced_features_and_security.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'advanced_features_and_security/view_books.html', {'books': books})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year, added_by=request.user)
        return redirect('view_books')
    return render(request, 'advanced_features_and_security/create_book.html')

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('view_books')
    return render(request, 'advanced_features_and_security/edit_book.html', {'book': book})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('view_books')
    return render(request, 'advanced_features_and_security/delete_book.html', {'book': book})

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
    from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    # Safe ORM query
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('publication_year')

        # Validate inputs (simple example)
        if title and author and year.isdigit():
            Book.objects.create(
                title=title,
                author=author,
                publication_year=int(year)
            )
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html')





