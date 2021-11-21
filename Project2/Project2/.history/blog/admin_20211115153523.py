from django.contrib import admin
from .models import Blog
from django import forms
# Register your models here.


class LessonForm(forms.Form):
    class Meta:
        model = Lesson
        fie
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_field = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
