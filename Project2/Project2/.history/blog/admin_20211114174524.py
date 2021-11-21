from django.contrib import admin
from .models import Blog
# Register your models here.

class Blog_admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'create_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']


admin.site.register(Blog, Blog_admin)
