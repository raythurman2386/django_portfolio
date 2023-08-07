from django.views.generic.base import TemplateView
from blog.models import Post

from services.models import Summary, Service, Contact

# Create your views here.


class ServicePageView(TemplateView):
    template_name = "services/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["summary_data"] = Summary.objects.all()
        context["service_data"] = Service.objects.all()
        context["contact_data"] = Contact.objects.all()
        context["blog_posts"] = Post.objects.order_by(
            '-created_at')[:8]
        return context
