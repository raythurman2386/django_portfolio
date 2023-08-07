from django.test import TestCase, RequestFactory
from django.urls import reverse
from services.models import Summary, Service, Contact
from services.views import ServicePageView


class ServicePageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Summary.objects.create(
            title="Test Summary", description="Test Description"
        )
        Service.objects.create(
            title="Test Service", description="Test Description"
        )
        Contact.objects.create(
            address="Test Address", email="test@example.com", phone="1234567890"
        )

    def test_service_page_view(self):
        factory = RequestFactory()
        request = factory.get(reverse("services"))
        view = ServicePageView()
        view.setup(request)
        context = view.get_context_data()

        # Check if the context data is correctly populated
        self.assertTrue("summary_data" in context)
        self.assertTrue("service_data" in context)
        self.assertTrue("contact_data" in context)
