from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from blog.models import Hero, Contact, Post
from blog.views import BlogPageView, PostDetailView


class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.hero = Hero.objects.create(
            title='Test Hero', description='This is a test hero.')
        self.contact = Contact.objects.create(
            address='Test Address',
            email='test@example.com',
            phone='1234567890'
        )
        self.post = Post.objects.create(
            id=1,
            title='Test Post',
            content='This is a test post content.',
            slug='test-post',
            author=self.user
        )

    def test_blog_page_view(self):
        view = BlogPageView.as_view()
        request = self.factory.get(reverse('blog:post-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)
        # Check the number of posts in the context
        self.assertEqual(len(response.context_data['posts']), 1)
        # Check the number of hero objects in the context
        self.assertEqual(response.context_data['hero'].count(), 1)
        # Check the number of contact objects in the context
        self.assertEqual(response.context_data['contact_data'].count(), 1)

        # Test pagination
        paginator = Paginator(response.context_data['posts'], 10)
        self.assertEqual(paginator.num_pages, 1)  # Check the number of pages

    def test_post_detail_view(self):
        view = PostDetailView.as_view()
        request = self.factory.get(
            reverse('blog:post-detail', kwargs={'pk': self.post.id}))
        response = view(request, pk=self.post.id)
        self.assertEqual(response.status_code, 200)
        # Check if the correct post object is in the context
        self.assertEqual(response.context_data['post'], self.post)
