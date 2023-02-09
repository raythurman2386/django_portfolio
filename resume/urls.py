from django.urls import path
from .views import ResumePageView

urlpatterns = [
    path('', ResumePageView.as_view()),
]
