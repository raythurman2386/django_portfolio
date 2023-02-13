from django.views.generic.base import TemplateView
from .models import Summary, Projects, Employment, Education, Skill, Contact, Resume_PDF
from django.http import FileResponse


class ResumePageView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary_data'] = Summary.objects.all()
        context['projects_data'] = Projects.objects.all()
        context['employment_data'] = Employment.objects.all()
        context['education_data'] = Education.objects.all()
        context['skill_data'] = Skill.objects.all()
        context['contact_data'] = Contact.objects.all()
        return context


def download_resume(request):
    resume = Resume_PDF.objects.all()
    print(resume)
    response = FileResponse(open(resume, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{resume.file.name}"'
    return response
