from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.documentation import include_docs_urls
from rest_framework import permissions

API_TITLE = "CTRL-SUN EMPLOYEES"
API_DESCRIPTION = "A Web API for adding users, branch locations and employee actions."
TERMS_OF_SERVICE = "https://somewhereoutthere.world"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("api.urls")),
    path('api-auth', include("rest_framework.urls")),
    path('api/v1/rest-auth/', include("rest_auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
