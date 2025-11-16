from django.urls import path
from .views import list_books, LibraryDetailView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
path("", include("relationship_app.urls")),

from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
