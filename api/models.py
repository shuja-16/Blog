from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['date']

