from http import HTTPStatus

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from core.forms import ContactForm


class AboutPageView(TemplateView):
    template_name = "best_works/about.html"


class ContactPageView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = "best_works/contacts.html"
    success_url = reverse_lazy("contact")
    success_message = (
        "Спасибо за Ваше сообщение! Мы свяжемся с Вами в ближайшее время"
    )


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
