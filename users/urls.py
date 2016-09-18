from django.conf.urls import url
from users.views import LoginView, LogoutView, HomeUserView, SignUpView

urlpatterns = [
    # Web URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup', SignUpView.as_view(), name='users_signup'),
    url(r'^$', HomeUserView.as_view(), name='users_home'),
]