from django.test import TestCase, RequestFactory
from django.urls import reverse
from portfolio.models import Hero, About, Project, Contact, ContactSubmission, Footer
from portfolio.views import IndexPageView, contact_submit
from portfolio.forms import ContactForm


class IndexPageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Hero.objects.create(
            title='Test Hero Title',
            subtitle='Test Hero Subtitle',
            description='Test Hero Description',
        )
        About.objects.create(
            title='Test About Title',
            description='Test About Description',
            icon='test-icon',
        )
        Project.objects.create(
            name='Test Project',
            description='Test Description',
            link='https://example.com',
        )
        Contact.objects.create(
            address='Test Address',
            email='test@email.com',
            phone='1231231234'
        )
        Footer.objects.create(
            copyright='© 2023'
        )
        # ... Create objects for other models as needed ...

    def test_index_page_view(self):
        # Create a request instance
        factory = RequestFactory()
        # Assuming 'index' is the URL name for the IndexPageView
        request = factory.get(reverse('index'))

        # Initialize the view with the request
        view = IndexPageView()
        view.setup(request)

        # Call the get_context_data() method
        context = view.get_context_data()

        # Assert that the context contains the expected data
        self.assertTrue('hero_data' in context)
        self.assertTrue('about_data' in context)
        self.assertTrue('project_data' in context)
        self.assertTrue('contact_data' in context)
        self.assertTrue('footer_data' in context)

        # ... Add more assertions to verify the content of the context data ...


class ContactSubmitViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'Test message',
        }

    def test_contact_submit_post_valid_form(self):
        # Create a request instance
        factory = RequestFactory()
        request = factory.post(reverse('contact_submit'), data=self.form_data)

        # Call the contact_submit view function
        response = contact_submit(request)

        # Verify the response
        self.assertEqual(response.status_code, 302)  # Redirect response
        self.assertEqual(response.url, '/')  # Verify the redirect URL

        # Verify that the contact submission is saved to the database
        submissions = ContactSubmission.objects.all()
        self.assertEqual(len(submissions), 1)
        submission = submissions[0]
        self.assertEqual(submission.name, self.form_data['name'])
        self.assertEqual(submission.email, self.form_data['email'])
        self.assertEqual(submission.message, self.form_data['message'])

    def test_contact_submit_get_request(self):
        # Create a request instance
        factory = RequestFactory()
        request = factory.get(reverse('contact_submit'))

        # Call the contact_submit view function
        response = contact_submit(request)

        # Verify the response
        self.assertEqual(response.status_code, 200)  # OK response

        # Verify that the response contains the contact form
        self.assertContains(response, '<form', count=1)
