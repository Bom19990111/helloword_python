from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
import blog

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs.as_view(), name='all_blogs'),
    path('<slug:slug>/', views.all_blogs.as_view(), name='detail')
]
