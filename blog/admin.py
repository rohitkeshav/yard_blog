from django.contrib import admin
from blog.models import Blog, Tags


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_content')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
