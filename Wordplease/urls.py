from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from blogs import urls as blogs_urls
from files.views import FileViewSet
from users import urls as users_urls
from posts import urls as posts_urls
from posts.views import PostView

router = DefaultRouter()
router.register('api/1.0/files', FileViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostView.as_view(), name="posts_home"),

    # blogs urls
    url(r'', include(blogs_urls)),

    # users urls
    url(r'', include(users_urls)),

    # posts urls
    url(r'', include(posts_urls)),

    # files urls
    url(r'', include(router.urls))
]
