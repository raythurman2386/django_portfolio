from django.urls import path
from .views import IndexPageView, contact_submit

urlpatterns = [
    path("contact/", contact_submit, name="contact_submit"),
    path("", IndexPageView.as_view(), name="index"),
]
