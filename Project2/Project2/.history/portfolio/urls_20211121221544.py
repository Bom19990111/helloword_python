from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
import blog

app_name = 'from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
import blog

app_name = 'portf'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<slug:slug>/', views.detail, name='detail')
]
'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<slug:slug>/', views.detail, name='detail')
]
