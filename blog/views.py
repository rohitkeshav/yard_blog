from .models import Blog
from .serializers import BlogSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class BlogViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )

    queryset = User.objects.all()
    serializer_class = UserSerializer
