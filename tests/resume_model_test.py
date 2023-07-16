from django.test import TestCase
from resume.models import (
    Summary,
    Projects,
    Employment,
    Education,
    Skill,
    Contact,
    Resume_PDF,
)


class SummaryModelTest(TestCase):
    def test_summary_model(self):
        summary = Summary.objects.create(
            title="Summary Title", description="Summary Description"
        )
        self.assertEqual(str(summary), "Summary Title")


class ProjectsModelTest(TestCase):
    def test_projects_model(self):
        project = Projects.objects.create(
            title="Project Title", description="Project Description"
        )
        self.assertEqual(str(project), "Project Title")


class EmploymentModelTest(TestCase):
    def test_employment_model(self):
        employment = Employment.objects.create(
            title="Employment Title",
            role="Employment Role",
            location="Employment Location",
            start_date="2023-01-01",
            end_date="2023-12-31",
            description="Employment Description",
        )
        self.assertEqual(str(employment), "Employment Title")


class EducationModelTest(TestCase):
    def test_education_model(self):
        education = Education.objects.create(
            title="Education Title",
            description="Education Description",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        self.assertEqual(str(education), "Education Title")


class SkillModelTest(TestCase):
    def test_skill_model(self):
        skill = Skill.objects.create(skill="Python")
        self.assertEqual(str(skill), "Python")


class ContactModelTest(TestCase):
    def test_contact_model(self):
        contact = Contact.objects.create(
            address="Contact Address", email="contact@example.com", phone="1234567890"
        )
        self.assertEqual(str(contact), "contact@example.com")


class ResumePDFModelTest(TestCase):
    def test_resumepdf_model(self):
        resumepdf = Resume_PDF.objects.create(title="Resume Title")
        self.assertEqual(str(resumepdf), "Resume Title")
