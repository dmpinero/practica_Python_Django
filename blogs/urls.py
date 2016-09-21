from django.conf.urls import url


from blogs.views import BlogsView, BlogsUserView, BlogPostDetailView
from posts.views import PostCreationView

urlpatterns = [
    url('^blogs$', BlogsView.as_view(), name='blogs_list'),
    url('^blogs/(?P<blog_username>[A-Za-z]+)/$', BlogsUserView.as_view(), name='blogs_user_list'),
    url('^blogs/(?P<blog_username>[A-Za-z]+)/(?P<post_id>[0-9]+)$', BlogPostDetailView.as_view(), name='blog_post_detail'),
]