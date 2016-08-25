from .models import Blog
from .serializers import BlogSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
