from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
import blog

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<slug:slug>/', views.detail.as_view(), name='blog_detail')
]
