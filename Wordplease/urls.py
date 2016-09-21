from django.conf.urls import url, include
from django.contrib import admin

from blogs import urls as blogs_urls
from users import urls as users_urls
from posts import urls as posts_urls
from posts.views import PostView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostView.as_view(), name="posts_home"),

    # blogs urls
    url(r'', include(blogs_urls)),

    # users urls
    url(r'', include(users_urls)),

    # posts urls
    url(r'', include(posts_urls))
]
