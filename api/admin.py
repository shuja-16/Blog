from django.contrib import admin
from api.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
