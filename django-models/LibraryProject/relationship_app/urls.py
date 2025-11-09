   # relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    # Book/Library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs using built-in class-based views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration uses custom view
    path('register/', views.register, name='register'),

    # Home page (optional)
    path('', views.home, name='home'),
]


urlpatterns = [
    # Book/Library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

urlpatterns = [
    # Book/Library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs using built-in views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Registration uses custom view
    path('register/', views.register, name='register'),

    # Home page (optional)
    path('', views.home, name='home'),
]


    # Authentication URLs
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),  # Protected home page
]

