from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, TemplateView

from core.forms import ContactForm
from core.models import About
from works.models import Achievement, Employee


@method_decorator(
    cache_page(settings.ABOUT_PAGE_CACHE_SECOND),
    name="dispatch",
)
class AboutPageView(TemplateView):
    template_name = "best_works/about.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["about_us"] = About.objects.first()
        data["employees"] = Employee.objects.all()
        data["achievements"] = Achievement.objects.all()

        return data


class ContactPageView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = "best_works/contacts.html"
    success_url = reverse_lazy("contacts")
    success_message = (
        "Спасибо за Ваше сообщение! Мы свяжемся с Вами в ближайшее время"
    )

    def form_valid(self, form) -> HttpResponseRedirect:
        response = super().form_valid(form)
        return response


class BadRequestView(TemplateView):
    template_name = "errors/400.html"

    def render_to_response(self, context, **response_kwargs):
        response_kwargs["status"] = 400
        return super().render_to_response(context, **response_kwargs)


class CsrfFailureView(TemplateView):
    template_name = "errors/403.html"

    def render_to_response(self, context, **response_kwargs):
        response_kwargs["status"] = 403
        return super().render_to_response(context, **response_kwargs)


class PageNotFoundView(TemplateView):
    template_name = "errors/404.html"

    def render_to_response(self, context, **response_kwargs):
        response_kwargs["status"] = 404
        return super().render_to_response(context, **response_kwargs)


def internal_server_error(request, *args, **argv):
    template_name: str = "errors/500.html"
    return render(request, template_name, status=500)
