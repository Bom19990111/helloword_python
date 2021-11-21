from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'create_on')
    list_filter = ('status',)
    search_field = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
