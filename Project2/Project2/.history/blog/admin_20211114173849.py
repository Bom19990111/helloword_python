from django.contrib import admin
from .models import Blog
# Register your models here.
admin.site.register(Blog)

class Blog_admin(admin.ModelAdmin):
    list = models.
