from django.urls import path, include, re_path
from django.views.static import serve
from apps.tools.helpers import schema_view
from django.contrib import admin

from sanx import settings

urlpatterns = [
    path('api/', include('apps.urls')),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
