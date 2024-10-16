from django.views.generic import ListView, TemplateView

from works.models import Service


class HomePageView(TemplateView):
    template_name = "works/index.html"


class ServiceView(ListView):
    template_name = "works/services.html"
    model = Service
    context_object_name = "services"
