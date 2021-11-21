from django.shortcuts import get_object_or_404, render
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.


def all_blogs(request):
    blogs = Blog.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(contact_list, 25)
    return render(request, 'blog/index.html', {'blogs': blogs})


def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', {'blog': blog})
    