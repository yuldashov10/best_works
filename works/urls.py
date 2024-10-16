from django.urls import path

from works.apps import WorksConfig
from works.views import HomePageView, ServiceView

app_name = WorksConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("services/", ServiceView.as_view(), name="services"),
]
