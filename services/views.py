from django.views.generic.base import TemplateView


# Create your views here.
class ServicePageView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['summary_data'] = Summary.objects.all()
        # context['projects_data'] = Projects.objects.all()
        # context['employment_data'] = Employment.objects.all()
        # context['education_data'] = Education.objects.all()
        # context['skill_data'] = Skill.objects.all()
        # context['contact_data'] = Contact.objects.all()
        return context