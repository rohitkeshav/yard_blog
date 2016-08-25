from django.contrib import admin
from blog.models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
