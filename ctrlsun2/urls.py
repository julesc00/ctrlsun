from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.documentation import include_docs_urls
from rest_framework import permissions

API_TITLE = "CTRL-SUN EMPLOYEES"
API_DESCRIPTION = "A Web API for adding users, branch locations and employee actions."
TERMS_OF_SERVICE = "https://somewhereoutthere.world"

schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version="v1",
        description=API_DESCRIPTION,
        terms_of_service=TERMS_OF_SERVICE
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('', include("api.urls")),
    path('api-auth/', include("rest_framework.urls")),
    path('rest-auth/', include("rest_auth.urls")),

    # Core app endpoints
    path('app/', include("core.urls")),

    path('docs/', include_docs_urls(
        title=API_TITLE,
        description=API_DESCRIPTION
    )),

    # To view documentation: /redoc/
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  # <-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # <-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
