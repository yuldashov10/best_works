from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, TemplateView

from works.models import Advantage, Review, Service, Slide


@method_decorator(
    cache_page(settings.HOME_PAGE_CACHE_SECOND),
    name="dispatch",
)
class HomePageView(TemplateView):
    template_name = "works/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["slides"] = Slide.objects.all()
        data["advantages"] = Advantage.objects.all()
        data["reviews"] = Review.objects.all()

        return data


class ServiceView(ListView):
    template_name = "works/services.html"
    model = Service
    context_object_name = "services"
