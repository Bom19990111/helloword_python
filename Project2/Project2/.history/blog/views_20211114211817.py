from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.


def all_blogs(request):
    blogs = Blog.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request):
    model
    return render(request, 'blog/detail.html')
    