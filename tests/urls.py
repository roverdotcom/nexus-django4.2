from django.conf.urls import include, url
from django.contrib import admin

import nexus

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^nexus/', include(nexus.site.urls)),
]
