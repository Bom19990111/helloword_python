from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views import generic

# Create your views here.
class BlogList(generic.ListView):
    queryset = Blog.objects.filter(status = 1).order_by('-created_on')