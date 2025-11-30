from .models import Book
from rest_framework import serializers
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Book API!"})

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

        fields = ['id', 'title', 'author']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
