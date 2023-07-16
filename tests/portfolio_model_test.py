from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from portfolio.models import (
    Hero,
    About,
    Tag,
    Project,
    Contact,
    ContactSubmission,
    Footer,
)


class HeroModelTest(TestCase):
    def setUp(self):
        self.hero = Hero.objects.create(
            title="Test Title",
            subtitle="Test Subtitle",
            description="Test Description",
            image="path/to/test/image.jpg",
        )

    def test_hero_fields(self):
        self.assertEqual(self.hero.title, "Test Title")
        self.assertEqual(self.hero.subtitle, "Test Subtitle")
        self.assertEqual(self.hero.description, "Test Description")
        self.assertEqual(self.hero.image, "path/to/test/image.jpg")

    def test_hero_str_representation(self):
        expected_str = "Test Title Test Subtitle"
        self.assertEqual(str(self.hero), expected_str)

    def test_hero_verbose_names(self):
        self.assertEqual(Hero._meta.verbose_name, "Hero")
        self.assertEqual(Hero._meta.verbose_name_plural, "Hero")

    def test_hero_instance(self):
        self.assertIsInstance(self.hero, Hero)


class AboutModelTest(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            title="Test Title", description="Test Description", icon="test-icon"
        )

    def test_about_fields(self):
        self.assertEqual(self.about.title, "Test Title")
        self.assertEqual(self.about.description, "Test Description")
        self.assertEqual(self.about.icon, "test-icon")

    def test_about_str_representation(self):
        self.assertEqual(str(self.about), "Test Title")

    def test_about_verbose_names(self):
        self.assertEqual(About._meta.verbose_name, "About")
        self.assertEqual(About._meta.verbose_name_plural, "About")

    def test_about_instance(self):
        self.assertIsInstance(self.about, About)


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_fields(self):
        self.assertEqual(self.tag.name, "Test Tag")

    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag), "Test Tag")

    def test_tag_instance(self):
        self.assertIsInstance(self.tag, Tag)


class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.project = Project.objects.create(
            name="Test Project",
            description="Test Description",
            link="https://example.com",
        )
        cls.tags = ["Tag 1", "Tag 2"]
        for tag in cls.tags:
            cls.project.tags.create(name=tag)

    def test_name_field(self):
        project = Project.objects.get(id=self.project.id)
        field_label = project._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_description_field(self):
        project = Project.objects.get(id=self.project.id)
        field_label = project._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_link_field(self):
        project = Project.objects.get(id=self.project.id)
        field_label = project._meta.get_field("link").verbose_name
        self.assertEquals(field_label, "link")

    def test_image_field_upload(self):
        image_path = "media/hero.jpg"
        uploaded_image = SimpleUploadedFile(
            name="hero.jpg",
            content=open(image_path, "rb").read(),
            content_type="image/jpeg",
        )
        project = Project.objects.create(
            name="Test Image Upload",
            description="Test Description",
            link="https://example.com",
            image=uploaded_image,
        )
        self.assertTrue(project.image.name.endswith(".jpg"))

    def test_tags_field(self):
        project = Project.objects.get(id=self.project.id)
        self.assertEquals(project.tags.count(), len(self.tags))
        for tag in self.tags:
            self.assertTrue(project.tags.filter(name=tag).exists())

    def test_str_representation(self):
        project = Project.objects.get(id=self.project.id)
        expected_str = project.name
        self.assertEquals(str(project), expected_str)


class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.contact = Contact.objects.create(
            address="123 Main St",
            email="contact@example.com",
            phone="123-456-7890",
        )

    def test_address_field(self):
        contact = Contact.objects.get(id=self.contact.id)
        field_label = contact._meta.get_field("address").verbose_name
        self.assertEquals(field_label, "address")

    def test_email_field(self):
        contact = Contact.objects.get(id=self.contact.id)
        field_label = contact._meta.get_field("email").verbose_name
        self.assertEquals(field_label, "email")

    def test_phone_field(self):
        contact = Contact.objects.get(id=self.contact.id)
        field_label = contact._meta.get_field("phone").verbose_name
        self.assertEquals(field_label, "phone")

    def test_str_representation(self):
        contact = Contact.objects.get(id=self.contact.id)
        expected_str = contact.email
        self.assertEquals(str(contact), expected_str)


class ContactSubmissionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.submission = ContactSubmission.objects.create(
            name="John Doe",
            email="john@example.com",
            message="Test message",
        )

    def test_name_field(self):
        submission = ContactSubmission.objects.get(id=self.submission.id)
        field_label = submission._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_email_field(self):
        submission = ContactSubmission.objects.get(id=self.submission.id)
        field_label = submission._meta.get_field("email").verbose_name
        self.assertEquals(field_label, "email")

    def test_message_field(self):
        submission = ContactSubmission.objects.get(id=self.submission.id)
        field_label = submission._meta.get_field("message").verbose_name
        self.assertEquals(field_label, "message")

    def test_timestamp_field(self):
        submission = ContactSubmission.objects.get(id=self.submission.id)
        field_label = submission._meta.get_field("timestamp").verbose_name
        self.assertEquals(field_label, "timestamp")

    def test_str_representation(self):
        submission = ContactSubmission.objects.get(id=self.submission.id)
        expected_str = submission.name
        self.assertEquals(str(submission), expected_str)


class FooterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.footer = Footer.objects.create(copyright="© 2023")

    def test_copyright_field(self):
        footer = Footer.objects.get(id=self.footer.id)
        field_label = footer._meta.get_field("copyright").verbose_name
        self.assertEquals(field_label, "copyright")

    def test_str_representation(self):
        footer = Footer.objects.get(id=self.footer.id)
        expected_str = footer.copyright
        self.assertEquals(str(footer), expected_str)
