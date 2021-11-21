from django.contrib import admin
from .models import Blog
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
# Register your models here.


class LessonForm(forms.Form):
    content 
    class Meta:
        model = Blog
        fields = '__all__'
        
class BlogAdmin(admin.ModelAdmin):
    forms = LessonForm
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_field = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
