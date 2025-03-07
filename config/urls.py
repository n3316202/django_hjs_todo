import mimetypes
from django.contrib import admin
from django.urls import include, path

import config
from config import settings


urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
    	path('__debug__/', include(debug_toolbar.urls))
    ]

