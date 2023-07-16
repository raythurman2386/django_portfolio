from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Hero, About, Project, Contact, ContactSubmission, Footer


class IndexPageView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hero_data"] = Hero.objects.all()
        context["about_data"] = About.objects.all()
        context["project_data"] = Project.objects.all()
        context["contact_data"] = Contact.objects.all()
        context["footer_data"] = Footer.objects.all()
        return context


def contact_submit(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Save to the db
            submission = ContactSubmission(name=name, email=email, message=message)
            submission.save()

            # Send an email notification
            subject = "*** PORTFOLIO: Contact Submission ***"
            email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            send_mail(
                subject,
                email_message,
                "raymondthurman5@gmail.com",
                ["raymondthurman5@gmail.com"],
            )

            # Replace with the URL for the success page
            return redirect("/")
    else:
        form = ContactForm()
    return render(request, "components/contact_form.html", {"form": form})
