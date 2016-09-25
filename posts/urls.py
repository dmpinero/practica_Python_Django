from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from blogs.api import BlogListAPI
from posts.api import PostViewSet
from posts.views import PostCreationView

# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/posts', PostViewSet, base_name='post')

urlpatterns = [
    url('^new-post$', PostCreationView.as_view(), name='posts_create'),

    # API URLS
    url(r'', include(router.urls)),  # Incluir las URLs de API
]