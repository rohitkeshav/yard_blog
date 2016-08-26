from .models import Blog, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogSerializer, CommentSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class BlogViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )

    queryset = User.objects.all()
    serializer_class = UserSerializer
