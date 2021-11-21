from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts') 
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    content = models.Texx

    def __str__(self):
        return self.title
