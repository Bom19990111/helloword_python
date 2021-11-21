from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

USE_TZ = False
class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts') 
    created_on = models.DateTimeField(
        auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

class meta:
    ordering = ['-created_on']


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''
def __str__(self):
    return self.title
