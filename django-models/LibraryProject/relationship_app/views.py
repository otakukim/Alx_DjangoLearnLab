from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView


# --------------------------
# Function-Based View (FBV)
# --------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# --------------------------
# Class-Based View (CBV)
# --------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"











