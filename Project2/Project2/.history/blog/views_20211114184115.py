from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.


dè all_blogs(request):
    blogs = Blog.objects.filter(status=1).order_by('-created_on')
    