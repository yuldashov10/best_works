from django.conf import settings
from django.urls import path
from django.views.decorators.cache import cache_page

from works.apps import WorksConfig
from works.views import HomePageView, ServiceView

app_name = WorksConfig.name

urlpatterns = [
    path(
        "",
        cache_page(settings.HOME_PAGE_CACHE_SECOND)(HomePageView.as_view()),
        name="home_page",
    ),
    path("services/", ServiceView.as_view(), name="services"),
]
