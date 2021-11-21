from django.shortcuts import get_object_or_404, render
from .models import Blog
from django.views import generic

# Create your views here.


class all_blogs(request):
    blogs = Blog.objects.filter(status=1).order_by('-created_on')
    