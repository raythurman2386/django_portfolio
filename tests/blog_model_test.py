from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Hero, Category, Tag, Post, Comment, Contact


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Test Category")
        self.tag = Tag.objects.create(name="Test Tag")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post content.",
            slug="test-post",
            author=self.user,
        )
        self.comment = Comment.objects.create(
            post=self.post, author=self.user, content="This is a test comment."
        )
        self.contact = Contact.objects.create(
            address="Test Address", email="test@example.com", phone="1234567890"
        )

    def test_hero_model(self):
        hero = Hero.objects.create(
            title="Test Hero", description="This is a test hero."
        )
        self.assertEqual(hero.title, "Test Hero")
        self.assertEqual(hero.description, "This is a test hero.")
        self.assertEqual(str(hero), "Test Hero")

    def test_category_model(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(str(self.category), "Test Category")

    def test_tag_model(self):
        self.assertEqual(self.tag.name, "Test Tag")
        self.assertEqual(str(self.tag), "Test Tag")

    def test_post_model(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post content.")
        self.assertEqual(self.post.slug, "test-post")
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.created_at.date(), timezone.now().date())
        self.assertEqual(str(self.post), "Test Post")

        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)
        self.assertEqual(self.post.categories.count(), 1)
        self.assertEqual(self.post.tags.count(), 1)

    def test_comment_model(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.content, "This is a test comment.")
        self.assertEqual(
            str(self.comment), f"Comment by {self.user.username} on {self.post.title}"
        )

    def test_contact_model(self):
        self.assertEqual(self.contact.address, "Test Address")
        self.assertEqual(self.contact.email, "test@example.com")
        self.assertEqual(self.contact.phone, "1234567890")
        self.assertEqual(str(self.contact), "test@example.com")
