from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import (
    AboutPageView,
    BadRequestView,
    ContactPageView,
    CsrfFailureView,
    PageNotFoundView,
)

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),
    path(
        "jet/dashboard/",
        include("jet.dashboard.urls", "jet-dashboard"),
    ),
    path("", include("works.urls", namespace="works")),
    path("about_us/", AboutPageView.as_view(), name="about_us"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )

handler400 = BadRequestView.as_view()
handler403 = CsrfFailureView.as_view()
handler404 = PageNotFoundView.as_view()
handler500 = "core.views.internal_server_error"
