from django.db import models
from django.conf import settings

class Publication(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=140, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Publication)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

class UserProfile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    
