from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.views import LoginView, LogoutView, HomeUserView, SignUpView
from users.api import UserViewSet

router = DefaultRouter()
router.register('^api/1.0/users', UserViewSet, base_name='api_users_')

urlpatterns = [
    # Web URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup', SignUpView.as_view(), name='users_signup'),
    url(r'^$', HomeUserView.as_view(), name='users_home'),

    # API URLS
    url(r'', include(router.urls))
]