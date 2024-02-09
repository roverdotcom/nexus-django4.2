from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

import nexus

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^nexus/', include(nexus.site.urls)),
]
