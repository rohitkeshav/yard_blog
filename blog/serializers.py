from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'comment')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
