from django.contrib.admin import site

from .models import Config

site.register(Config)
