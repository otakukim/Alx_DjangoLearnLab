from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookListCreateAPIView, BookViewSet, home

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', home, name='home'),  # root path
    path('books/', BookList.as_view(), name='book-list'),  # ListAPIView
    path('books-create/', BookListCreateAPIView.as_view(), name='book-list-create'),  # optional create endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),  # CRUD via ViewSet
]

