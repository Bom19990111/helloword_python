from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


def home(request):
    return render(request, 'portfolio/detail.html', {'blog': blog})
