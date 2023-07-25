from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("", include("portfolio.urls")),
    path("resume/", include("resume.urls")),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path('accounts/', include('allauth.urls')),
    path("blog/", include("blog.urls"), name="blog"),
    path("admin/", admin.site.urls, name="django_admin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
