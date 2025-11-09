
   # relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Book/Library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # Protected home page
]

