from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'

USE_I18N = True

USE_L10N = False

USE_TZ = False
class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts') 
    created_on = models.DateTimeField(
        auto_now_add=True, DATETIME_FORMAT="%Y-%m-%d %H:%M:%S")
    update_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

class meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title