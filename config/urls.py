from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('', include('portfolio.urls'), name='home'),
    path('resume/', include('resume.urls'), name='resume'),
    path('admin/', admin.site.urls, name='django_admin'),
    path('cms/', include(wagtailadmin_urls), name='cms_admin'),
    path('documents/', include(wagtaildocs_urls), name='docs'),
    path('pages/', include(wagtail_urls), name='pages'),
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
