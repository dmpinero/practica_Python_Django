from django.conf.urls import url, include
from blogs.views import BlogsView, BlogsUserView, BlogPostDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/1.0/photos', BlogsViewSet, base_name='api_photos')

urlpatterns = [
    # Web URLS
    url('^blogs$', BlogsView.as_view(), name='blogs_list'),
    url('^blogs/(?P<blog_username>[A-Za-z]+)/$', BlogsUserView.as_view(), name='blogs_user_list'),
    url('^blogs/(?P<blog_username>[A-Za-z]+)/(?P<post_id>[0-9]+)$', BlogPostDetailView.as_view(), name='blog_post_detail'),

    # API URLS
    url(r'', include(router.urls))
]