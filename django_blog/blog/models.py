from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(model.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    published_date = models.IntegerField()
