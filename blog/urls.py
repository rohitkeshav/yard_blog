from django.conf.urls import url
from rest_framework import routers
from .views import BlogViewSet, CommentViewSet, UserViewSet

router = routers.SimpleRouter()

router.register(r'blog_endpoint', BlogViewSet)
router.register(r'comment_endpoint', CommentViewSet)
router.register(r'user_endpoint', UserViewSet)

front_end_urls = []

urlpatterns = router.urls + front_end_urls
