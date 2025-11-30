from django.urls import path ,include
from .views import BookListCreateAPIView, BookViewSet,home
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    
    path('', home, name='home'),  # root path for the API app
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # token retrieval
    ]