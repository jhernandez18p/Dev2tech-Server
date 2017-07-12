from django.conf import settings
from django.conf.urls import ( url, include, handler404, handler500, handler403, handler400 )
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

from local_apps.frontend.views import (Redirect, lang)

handler404 = 'local_apps.authentication.views.my_custom_page_not_found_view'
handler500 = 'local_apps.authentication.views.my_custom_error_view'
handler403 = 'local_apps.authentication.views.my_custom_permission_denied_view'
handler400 = 'local_apps.authentication.views.my_custom_bad_request_view'

sitemaps = {
#    'products': ProductSitemap(),
   'static': StaticSitemap(),
}

urlpatterns = [
    url(r'^$', Redirect.as_view()),
    url(r'^lang$', lang, name='lang'),
    url(r'^es/', include('local_apps.frontend.es_urls', namespace='es')),
    url(r'^en/', include('local_apps.frontend.en_urls', namespace='en')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('local_apps.api.urls', namespace='rest_framework')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'Dev2tech Admin'
admin.site.site_header = 'Dev2tech Admin'