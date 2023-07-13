from django.test import TestCase, RequestFactory
from django.urls import reverse
from resume.models import Summary, Projects, Employment, Education, Contact, Skill, Resume_PDF
from resume.views import ResumePageView


class DownloadResumeViewTest(TestCase):
    def test_download_resume(self):
        response = self.client.get(reverse('download_resume'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get('Content-Disposition'),
            'attachment; filename="RayThurmanResume.pdf"'
        )


class ResumePageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Summary.objects.create(
            title='Test Resume Title',
            description='Test Resume Description'
        )
        Projects.objects.create(
            title='Test Project',
            description='Test Description'
        )
        Employment.objects.create(
            title='Test Title',
            role='Test Role',
            location='Test Location',
            description='Test Description',
            start_date='2023-01-01',
            end_date='2023-01-01'
        )
        Education.objects.create(
            title='Test Title',
            description='Test Description',
            start_date='2023-01-01',
            end_date='2023-01-01'
        )
        Skill.objects.create(
            skill='Test Skill'
        )
        Contact.objects.create(
            address='Test Address',
            email='test@email.com',
            phone='1231231234'
        )

    def test_resume_page_view(self):
        factory = RequestFactory()
        request = factory.get(reverse('resume'))
        view = ResumePageView()
        view.setup(request)
        context = view.get_context_data()

        self.assertTrue('summary_data' in context)
        self.assertTrue('projects_data' in context)
        self.assertTrue('employment_data' in context)
        self.assertTrue('education_data' in context)
        self.assertTrue('skill_data' in context)
        self.assertTrue('contact_data' in context)
