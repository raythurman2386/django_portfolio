from django.test import TestCase, Client
from django.urls import reverse
from services.models import Summary, Service, Contact


class ServicePageViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_service_page_view_context(self):
        # Create sample data for Summary, Service, and Contact models
        summary = Summary.objects.create(
            title="Test Summary", description="Test Description"
        )
        service = Service.objects.create(
            title="Test Service", description="Test Description"
        )
        contact = Contact.objects.create(
            address="Test Address", email="test@example.com", phone="1234567890"
        )

        # Simulate a request to the ServicePageView
        response = self.client.get(reverse("services"))

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the context data is correctly populated
        self.assertEqual(len(response.context["summary_data"]), 1)
        self.assertEqual(len(response.context["service_data"]), 1)
        self.assertEqual(len(response.context["contact_data"]), 1)

        # Check the values of specific objects
        self.assertEqual(response.context["summary_data"][0].title, "Test Summary")
        self.assertEqual(response.context["service_data"][0].title, "Test Service")
        self.assertEqual(response.context["contact_data"][0].email, "test@example.com")
