from django.urls import path
from .views import ResumePageView, download_resume

urlpatterns = [
    path('', ResumePageView.as_view()),
    path('download', download_resume, name="download_resume"),
]
