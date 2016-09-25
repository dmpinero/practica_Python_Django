from django.conf.urls import url, include
from blogs.api import BlogListAPI
from blogs.views import BlogsView, BlogsUserView, BlogPostDetailView
from blogs.api import PostsAPIView

# TODO: Refactorizar URLs utilizando routers
# TODO: Separar URLs en 2 archivos: uno para api y otro para web


urlpatterns = [
    # Web URLS
    url('^blogs/$', BlogsView.as_view(), name='blogs_list'),
    url('^blogs/(?P<blog_username>[A-Za-z]+)/$', BlogsUserView.as_view(), name='blogs_user_list'),
    url('^blogs/(?P<blog_username>[A-Za-z]+)/(?P<post_id>[0-9]+)$', BlogPostDetailView.as_view(), name='blog_post_detail'),

    # API URLS
    url('^api/1.0/blogs/(?P<blog_username>[A-Za-z]+)/$', PostsAPIView.as_view(), name='posts_blog'),
    url('^api/1.0/blogs/$', BlogListAPI.as_view(), name='blog_list_api'),
]