from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
import portfolio

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('introduce/', views.introduce, name='introduce'),
    path('cv/', views.cv, name='cv'),
]
