from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from core.sitemaps import (
    StaticViewSitemap,
    ProjectSitemap,
)


sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
}


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('core.urls')
    ),

    path(
        'sitemap.xml',
        sitemap,
        {
            'sitemaps': sitemaps
        },
        name='django.contrib.sitemaps.views.sitemap'
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )