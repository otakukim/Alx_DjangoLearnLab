from django.db import models

# Create your models here.
class Post(models.Model):
	title: models.CharField(max_length=200)
	content: models.TextField()
	published_date: models.DateTimeField(auto_now_add=True)
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
