from django.conf.urls import url
from rest_framework import routers
from .views import BlogViewSet

router = routers.SimpleRouter()

router.register(r'blog_endpoint', BlogViewSet)

front_end_urls = []

urlpatterns = router.urls + front_end_urls
