# https://ryangallen.gitbooks.io/django-girls/content/ru/django_admin/index.html

from django.contrib import admin
from .models import Post

admin.site.register(Post)

