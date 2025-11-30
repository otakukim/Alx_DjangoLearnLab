from .models import Book
from rest_framework import serializers
from django.http import JsonResponse
from .models import Author, Book

def home(request):
    return JsonResponse({"message": "Welcome to the Book API!"})

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
