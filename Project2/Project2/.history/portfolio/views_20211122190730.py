from django.shortcuts import get_object_or_404, render
# from .models import home
from django.core.paginator import Paginator


def home(request):
  return render(request, 'portfolio/home.html')


def introduce(request):
  return render(request, 'portfolio/introduce.html')
def introduce(request):
  return render(request, 'portfolio/introduce.html')