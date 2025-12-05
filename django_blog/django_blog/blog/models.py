from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title: models.CharField(max_length=200) # type: ignore
	content: models.TextField() # type: ignore
	published_date: models.DateTimeField(auto_now_add=True) # type: ignore
	author: models.ForeignKey

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['created_at']
def __str__(self):

    return self.title

class User(models.Model):
	author_name = models.CharField(max_length=200)