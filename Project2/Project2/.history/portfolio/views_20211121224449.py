from django.shortcuts import get_object_or_404, render
from .models import home
from django.core.paginator import Paginator

def home(request):
    return (request, 'portfolio/home.html')