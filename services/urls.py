from django.urls import path
from .views import ServicePageView

urlpatterns = [
    path("", ServicePageView.as_view(), name="services"),
]
