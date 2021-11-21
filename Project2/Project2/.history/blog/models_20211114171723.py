from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(User)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
