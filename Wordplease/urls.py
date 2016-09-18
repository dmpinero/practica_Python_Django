from django.conf.urls import url, include
from django.contrib import admin

from users import urls as users_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # users urls
    url(r'', include(users_urls))
]
