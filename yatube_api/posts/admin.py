from django.contrib import admin

from .models import Follow, Group, Post

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Follow)
