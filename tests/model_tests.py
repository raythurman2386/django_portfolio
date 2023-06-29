from django.test import TestCase
from portfolio.models import Hero, About, Tag, Project, Contact, ContactSubmission, Footer


class HeroModelTest(TestCase):

    def setUp(self):
        self.hero = Hero.objects.create(
            title='Test Title',
            subtitle='Test Subtitle',
            description='Test Description',
            image='path/to/test/image.jpg'
        )

    def test_hero_fields(self):
        self.assertEqual(self.hero.title, 'Test Title')
        self.assertEqual(self.hero.subtitle, 'Test Subtitle')
        self.assertEqual(self.hero.description, 'Test Description')
        self.assertEqual(self.hero.image, 'path/to/test/image.jpg')

    def test_hero_str_representation(self):
        expected_str = 'Test Title Test Subtitle'
        self.assertEqual(str(self.hero), expected_str)

    def test_hero_verbose_names(self):
        self.assertEqual(Hero._meta.verbose_name, 'Hero')
        self.assertEqual(Hero._meta.verbose_name_plural, 'Hero')

    def test_hero_instance(self):
        self.assertIsInstance(self.hero, Hero)


class AboutModelTest(TestCase):

    def setUp(self):
        self.about = About.objects.create(
            title='Test Title',
            description='Test Description',
            icon='test-icon'
        )

    def test_about_fields(self):
        self.assertEqual(self.about.title, 'Test Title')
        self.assertEqual(self.about.description, 'Test Description')
        self.assertEqual(self.about.icon, 'test-icon')

    def test_about_str_representation(self):
        self.assertEqual(str(self.about), 'Test Title')

    def test_about_verbose_names(self):
        self.assertEqual(About._meta.verbose_name, 'About')
        self.assertEqual(About._meta.verbose_name_plural, 'About')

    def test_about_instance(self):
        self.assertIsInstance(self.about, About)
