from django.urls import path
from .views import PostDetailView, BlogPageView, add_comment

app_name = 'blog'

urlpatterns = [
    path('', BlogPageView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', add_comment, name='add-comment')
]
