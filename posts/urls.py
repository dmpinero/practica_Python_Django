from django.conf.urls import url
from posts.views import PostCreationView

urlpatterns = [
    url('^new-post$', PostCreationView.as_view(), name='posts_create'),
]