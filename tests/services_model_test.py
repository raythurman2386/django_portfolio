from django.test import TestCase
from services.models import Summary, Service, Contact


class SummaryModelTest(TestCase):
    def test_summary_model_str(self):
        summary = Summary.objects.create(
            title="Test Summary", description="Test Description"
        )
        self.assertEqual(str(summary), "Test Summary")


class ServiceModelTest(TestCase):
    def test_service_model_str(self):
        service = Service.objects.create(
            title="Test Service", description="Test Description"
        )
        self.assertEqual(str(service), "Test Service")


class ContactModelTest(TestCase):
    def test_contact_model_str(self):
        contact = Contact.objects.create(
            address="Test Address", email="test@example.com", phone="1234567890"
        )
        self.assertEqual(str(contact), "test@example.com")
