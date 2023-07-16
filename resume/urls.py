from django.urls import path
from .views import ResumePageView, download_resume

urlpatterns = [
    path("", ResumePageView.as_view(), name="resume"),
    path("download", download_resume, name="download_resume"),
]
