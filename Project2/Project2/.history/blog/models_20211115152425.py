from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import Rich


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

USE_TZ = False
class Blog(models.Model):
    title = models.CharField('Tiêu đề', max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts') 
    created_on = models.DateTimeField('Giờ tạo',
        auto_now_add=True)
    update_on = models.DateTimeField('Giờ cập nhật', auto_now=True)
    content = models.TextField()
    status = models.IntegerField('Trạng thái', choices=STATUS, default=0)

class meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title
