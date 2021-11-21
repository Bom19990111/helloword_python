from django.contrib import admin
from .models import Blog
from django.contrib import admin
# Register your models here.

class Lesson(admin.Model):
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_field = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
