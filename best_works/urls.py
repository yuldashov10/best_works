from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),
    path(
        "jet/dashboard/",
        include("jet.dashboard.urls", "jet-dashboard"),
    ),
    path("", include("works.urls", namespace="works")),
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

# handler404 = "views.func_name_for_404"
# handler403 = "views.func_name_for_403"
# handler500 = "views.func_name_for_500"
