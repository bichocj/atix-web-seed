from django.contrib.admin import site

from main.models import Post, Category

site.register(Category)



site.register(Post)
