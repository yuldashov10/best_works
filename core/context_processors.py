from typing import Any

from django.conf import settings
from django.core.cache import cache
from django.http import HttpRequest

from core.models import Company


def get_all_data_about_company(request: HttpRequest) -> dict[str, Any]:
    company_data: dict[str, Any] = cache.get("company_data")

    if not company_data:
        company = (
            Company.objects.select_related(
                "address",
                "opening_hours",
                "meta_tags",
            )
            .prefetch_related("social_networks")
            .first()
        )

        if company:
            company_data = {
                "company": company,
                "social_networks": list(company.social_networks.all()),
                "address": company.address.get_full_address,
                "opening_hours": company.opening_hours.get_full_opening_hour,
                "meta_tags": company.meta_tags,
            }

            cache.set(
                "company_data",
                company_data,
                settings.CONTEXT_DATA_CACHE_TIME_SECOND,
            )

    return company_data or {}
