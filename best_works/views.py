from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from best_works.forms import ContactForm


class AboutPageView(TemplateView):
    template_name = "best_works/about.html"


class ContactPageView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = "best_works/contacts.html"
    success_url = reverse_lazy("contact")
    success_message = (
        "Спасибо за Ваше сообщение! Мы свяжемся с Вами в ближайшее время"
    )
