# social_media_api/posts/admin.py

from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)