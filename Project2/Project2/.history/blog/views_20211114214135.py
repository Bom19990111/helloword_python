from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.


def base(request):
    return render(request, 'blog/base.html', {'blogs': blogs})

def all_blogs(request):
    blogs = Blog.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/base.html', {'blogs': blogs})


def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', {'blog': blog})
    