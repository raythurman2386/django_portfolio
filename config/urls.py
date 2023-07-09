from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('portfolio.urls'), name='home'),
    path('resume/', include('resume.urls'), name='resume'),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls, name='django_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
